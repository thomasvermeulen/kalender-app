# Kalender.io 📅

Kalender.io is een **Flask-gebaseerde webapplicatie** waarmee gebruikers agenda's kunnen beheren en evenementen kunnen toevoegen, bekijken en aanpassen. De applicatie ondersteunt verschillende gebruikersrollen, inclusief admin-functionaliteiten.

## 🚀 Functionaliteiten

### 🎯 Gebruikersfuncties
- Agenda's **maken, bekijken en beheren**.
- Evenementen **toevoegen, aanpassen en verwijderen**.

### 🔧 Adminfuncties
- **Overzicht van alle agenda's en gebruikers**.
- **Gebruikers beheren** (toevoegen/verwijderen).

### 👀 Bezoekersfuncties
- **Agenda's en evenementen bekijken zonder in te loggen**.

### 🌟 Algemeen
- **Paginering** voor agenda's en evenementen.
- **Responsive design** voor desktop en mobiel.
- **Veiligheid**: bcrypt voor wachtwoordhashing.
- **Filters** op evenementen (datum, locatie, zoektermen).

## 🛠 Installatie

Volg deze stappen om de applicatie lokaal te draaien:

1. **Clone de repository**:
   ```bash
   git clone https://github.com/thomasvermeulen/kalender-app/
   cd kalender.io
   ```
2. **Maak een virtuele omgeving aan en activeer deze**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Voor Mac/Linux
   venv\Scripts\activate   # Voor Windows
   ```
3. **Installeer vereiste pakketten**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Start de applicatie**:
   ```bash
   flask run
   ```

## 🏗 Gebruik

1. **Bezoek de applicatie**:
   - **Bezoekers**: Directe toegang tot agenda's en evenementen.
   - **Gebruikers**: Log in om agenda's te beheren.
   - **Admins**: Beheer gebruikers en agenda's via de adminpagina.

2. **Filters toepassen**:
   - Gebruik de zoekbalk om te filteren op **datum, locatie en naam**.

3. **Testaccounts**:
   - **Gebruiker**:
     - **Gebruikersnaam**: `Leerkracht2`
     - **Wachtwoord**: `HRUser`
   - **Admin**:
     - **Gebruikersnaam**: `Leerkracht`
     - **Wachtwoord**: `HRAdmin`

## ⚙️ Technologieën

- **Back-end**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, Jinja2, Bootstrap
- **Authenticatie**: bcrypt voor wachtwoordhashing

## 🖼️ Screenshots

### 🔑 Inlogpagina
![Inlogpagina Screenshot](https://cdn.discordapp.com/attachments/1096212248399204375/1330643363095117874/image.png?ex=67a47a73&is=67a328f3&hm=85dcbc3f09a8f82a490853b504916d104fcdc84584d611adcf3b337ecc9ad321&)

### 📊 Dashboard
![Dashboard Screenshot](https://cdn.discordapp.com/attachments/1096212248399204375/1330643641034870886/image.png?ex=67a47ab6&is=67a32936&hm=1ce79f65d8ce203be9476a150a7eaf1fe4466ac0bfb80df2f750d2abd8ff6d03&)

### 🛠 Admin Dashboard
![Admin Dashboard Screenshot](https://cdn.discordapp.com/attachments/1096212248399204375/1330643882333175888/image.png?ex=67a47aef&is=67a3296f&hm=009a944ea3474ed174c54a61a98a481e352fbb14b0f5ab00afe65a1fa9149e02&)

## 📚 Bronnenlijst

- **Achtergrond**: [papers.co](https://papers.co/desktop/vy76-wave-color-purple-pattern-background)
- **Code formatter**:  [formatter.org](https://formatter.org/)

👨‍💻 **Gemaakt door Thomas Vermeulen**. Feedback en bijdragen zijn altijd welkom! 🚀

