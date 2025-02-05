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
![Inlogpagina Screenshot](https://media.discordapp.net/attachments/1096212248399204375/1330643363095117874/image.png?ex=678eb9b3&is=678d6833&hm=200b54605cc310b57894fb82342b7f5e58b08404aa8ead21e1962b2e630f76b8&=&format=webp&quality=lossless&width=1440&height=653)

### 📊 Dashboard
![Dashboard Screenshot](https://media.discordapp.net/attachments/1096212248399204375/1330643641034870886/image.png?ex=678eb9f6&is=678d6876&hm=f8c6e58c47c2fef35f443540da2b62dbfdeaceb05db8f6135784da0244c8009d&=&format=webp&quality=lossless&width=1440&height=652)

### 🛠 Admin Dashboard
![Admin Dashboard Screenshot](https://media.discordapp.net/attachments/1096212248399204375/1330643882333175888/image.png?ex=678eba2f&is=678d68af&hm=885e7afaae0f06137109d0f7c52328567e7c2229a5cc42cc3858719aaf27b511&=&format=webp&quality=lossless&width=1440&height=652)

## 📚 Bronnenlijst

- **Achtergrond**: [papers.co](https://papers.co/desktop/vy76-wave-color-purple-pattern-background)
- **Code formatter**:  [formatter.org](https://formatter.org/)

👨‍💻 **Gemaakt door JOUW NAAM**. Feedback en bijdragen zijn altijd welkom! 🚀

