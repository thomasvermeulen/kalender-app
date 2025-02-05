from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "appelboom43!"


def db_connection():
    conn = sqlite3.connect("database/test.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))

    page = request.args.get("page", 1, type=int)
    per_page = 12
    offset = (page - 1) * per_page

    conn = db_connection()

    if session.get("is_admin") == 1:
        total_agendas = conn.execute("SELECT COUNT(*) FROM agendas").fetchone()[
            0
        ]
        agendas = conn.execute(
            """
            SELECT agendas.*, users.username 
            FROM agendas 
            JOIN users ON agendas.user_id = users.id 
            LIMIT ? OFFSET ?
            """,
            (per_page, offset),
        ).fetchall()
    else:
        total_agendas = conn.execute(
            "SELECT COUNT(*) FROM agendas WHERE user_id = ?",
            (get_user_id(session["username"]),),
        ).fetchone()[0]
        agendas = conn.execute(
            """
            SELECT agendas.*, users.username 
            FROM agendas 
            JOIN users ON agendas.user_id = users.id 
            WHERE agendas.user_id = ? 
            LIMIT ? OFFSET ?
            """,
            (get_user_id(session["username"]), per_page, offset),
        ).fetchall()

    conn.close()

    total_pages = (total_agendas + per_page - 1) // per_page

    return render_template(
        "dashboard.html",
        username=session["username"],
        agendas=agendas,
        page=page,
        total_pages=total_pages,
        is_admin=session.get("is_admin", 0),
    )


def get_user_id(username):
    conn = db_connection()
    user = conn.execute(
        "SELECT id FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return user["id"]


@app.context_processor
def inject_helpers():
    return dict(get_user_id=get_user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    error_message = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if not user:
            error_message = "Gebruikersnaam bestaat niet."
        elif not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            error_message = "Onjuist wachtwoord."
        else:
            session["username"] = user["username"]
            session["is_admin"] = user["is_admin"]
            return redirect(url_for("index"))

    return render_template("login.html", error_message=error_message)


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Je bent uitgelogd.", "info")
    return redirect(url_for("login"))


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" not in session or session.get("is_admin") != 1:
        flash("Je hebt geen toegang tot deze pagina.", "error")
        return redirect(url_for("index"))

    page = request.args.get("page", 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page

    conn = db_connection()
    total_users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    users = conn.execute(
        "SELECT * FROM users LIMIT ? OFFSET ?", (per_page, offset)
    ).fetchall()
    conn.close()

    total_pages = (total_users + per_page - 1) // per_page

    return render_template(
        "admin.html", users=users, page=page, total_pages=total_pages
    )


@app.route("/admin/gebruiker_toevoegen", methods=["POST"])
def add_user():
    username = request.form.get("username")
    password = request.form.get("password")
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    is_admin = 1 if request.form.get("is_admin") else 0

    conn = db_connection()
    conn.execute(
        "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
        (username, hashed_password, is_admin),
    )
    conn.commit()
    conn.close()

    flash("Gebruiker toegevoegd!", "success")
    return redirect(url_for("admin"))


@app.route("/admin/delete_user", methods=["POST"])
def delete_user():
    if "username" not in session or session.get("is_admin") != 1:
        flash("Je hebt geen toegang.", "error")
        return redirect(url_for("index"))

    user_id = request.form.get("user_id")

    conn = db_connection()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    flash("Gebruiker verwijderd!", "success")
    return redirect(url_for("admin"))


@app.route("/agenda/nieuw", methods=["GET", "POST"])
def add_agenda():
    if request.method == "POST":
        url_name = request.form.get("url_name")
        title = request.form.get("title")
        user_id = get_user_id(session["username"])

        conn = db_connection()
        conn.execute(
            "INSERT INTO agendas (url_name, title, user_id) VALUES (?, ?, ?)",
            (url_name, title, user_id),
        )
        conn.commit()
        conn.close()

        flash("Nieuwe agenda succesvol toegevoegd!", "success")
        return redirect(url_for("index"))

    return render_template("addcalendar.html")


@app.route("/agenda/<string:url_name>")
def view_agenda(url_name):
    conn = db_connection()
    agenda = conn.execute(
        "SELECT * FROM agendas WHERE url_name = ?", (url_name,)
    ).fetchone()

    if not agenda:
        flash("Agenda niet gevonden.", "error")
        conn.close()
        return redirect(url_for("index"))

    search_query = request.args.get("search", "").lower()
    limit = request.args.get("limit", 20, type=int)
    date_filter = request.args.get("date", "")
    location_filter = request.args.get("location", "").lower()

    query = "SELECT * FROM events WHERE agenda_id = ?"
    params = [agenda["id"]]

    if search_query:
        query += " AND LOWER(name) LIKE ?"
        params.append(f"%{search_query}%")

    if date_filter:
        query += " AND event_date = ?"
        params.append(date_filter)

    if location_filter:
        query += " AND LOWER(location) LIKE ?"
        params.append(f"%{location_filter}%")

    query += " ORDER BY event_date ASC, start_time ASC LIMIT ?"
    params.append(limit)

    count_query = query.replace("*", "COUNT(*)")
    count_query = count_query[: count_query.lower().find(" limit ")]
    total_events = conn.execute(count_query, params[:-1]).fetchone()[0]

    events = conn.execute(query, params).fetchall()
    conn.close()

    has_more = total_events > limit

    return render_template(
        "events.html",
        agenda=agenda,
        events=events,
        has_more=has_more,
        current_limit=limit,
        search_query=search_query,
    )


@app.route("/event/edit/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    conn = db_connection()
    event = conn.execute(
        "SELECT * FROM events WHERE id = ?", (event_id,)
    ).fetchone()

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        event_date = request.form.get("event_date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")
        location = request.form.get("location")

        conn.execute(
            "UPDATE events SET name = ?, description = ?, event_date = ?, start_time = ?, end_time = ?, location = ? WHERE id = ?",
            (
                name,
                description,
                event_date,
                start_time,
                end_time,
                location,
                event_id,
            ),
        )
        conn.commit()
        conn.close()

        flash("Event succesvol bijgewerkt!", "success")
        return redirect(url_for("view_agenda", url_name=event["agenda_id"]))

    conn.close()
    return render_template("edit_event.html", event=event)


@app.route("/agenda/<int:agenda_id>/nieuw_event", methods=["GET", "POST"])
def add_event(agenda_id):
    if "username" not in session:
        flash("Je moet ingelogd zijn om een evenement toe te voegen.", "error")
        return redirect(url_for("login"))

    conn = db_connection()
    agenda = conn.execute(
        "SELECT * FROM agendas WHERE id = ?", (agenda_id,)
    ).fetchone()

    if not agenda:
        flash("Agenda niet gevonden.", "error")
        conn.close()
        return redirect(url_for("index"))

    if session.get("is_admin") != 1 and agenda["user_id"] != get_user_id(
        session["username"]
    ):
        flash("Je hebt geen toegang tot deze agenda.", "error")
        conn.close()
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        event_date = request.form.get("event_date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")
        location = request.form.get("location")

        conn.execute(
            """
            INSERT INTO events (name, description, event_date, start_time, end_time, location, agenda_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                description,
                event_date,
                start_time,
                end_time,
                location,
                agenda_id,
            ),
        )
        conn.commit()
        conn.close()

        flash("Nieuw evenement toegevoegd!", "success")
        return redirect(url_for("view_agenda", url_name=agenda["url_name"]))

    conn.close()
    return render_template("add_event.html", agenda=agenda)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)