# PO Meesterproef — Week 4 (Formulier koppelen aan SQLite)

Startertemplate (HTML/CSS + Flask + SQLite) voor de PO Meesterproef.
Dit is de **week 4**-versie: een HTML-formulier koppelen aan de SQLite-database (INSERT + SELECT).
Je mag een eigen onderwerp kiezen.

> Dit is een **template repository**. Klik op **"Use this template"** → **"Create a new repository"** om je eigen kopie te maken. Daarna werk je in jouw eigen repo.

## Wat zit erin?

```
pomeesterproef-week4/
├── app.py              # Flask-app (routes "/", "/data", "/toevoegen", "/laad-basisdata")
├── database.py         # SQLite-koppeling (init, seed, SELECT, INSERT)
├── requirements.txt    # Python-dependencies
├── data.db             # SQLite-database (wordt aangemaakt, in .gitignore)
├── templates/
│   ├── index.html      # Homepage
│   ├── data.html       # Pagina met data uit de database
│   └── toevoegen.html  # Formulier om data toe te voegen
├── static/
│   ├── css/style.css   # Basis styling
│   └── js/script.js    # JavaScript (wordt later toegevoegd)
└── .gitignore
```

## Vereisten

- Python 3.10 of hoger
- Git (zie hieronder)
- Een editor (bijv. VS Code)

## Project starten (lokaal)

> **Let op:** Je hebt al een eigen project (`pomeesterproef-jouwnaam`) uit de vorige opdrachten. Daar werk je in verder. De nieuwe template (week 4) gebruik je als **voorbeeld**: maak daarvoor een **nieuwe map** aan en clone de template daarin.

Stappen voor het voorbeeld (week 4 template):
1. Maak een nieuwe map aan en ga erin:
   ```bash
   mkdir pomeesterproef-week4-voorbeeld
   cd pomeesterproef-week4-voorbeeld
   ```
2. Clone de template in deze map:
   ```bash
   git clone git@github.com:arhc-informatica/pomeesterproef-week4.git .
   ```
   Controleer dat je in de map zit waar `app.py` staat (`ls` / `dir`).

Daarna in die map uitvoeren:

```bash
# 1. Virtuele omgeving aanmaken
python3 -m venv .venv

# 2. Activeren
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 3. Dependencies installeren
pip install -r requirements.txt

# 4. App starten
python app.py
```

Open daarna http://127.0.0.1:5000 in je browser.

> **Verder werken in je eigen project:** kopieer de nieuwe bestanden (`database.py` met `voeg_item_toe`, de routes in `app.py`, `templates/data.html` en `templates/toevoegen.html`) uit het voorbeeld naar je bestaande `pomeesterproef-jouwnaam`-map. Commit en push daarna in je eigen repo.

## Git voor beginners — stap voor stap

> Git, je identiteit en SSH-key heb je al in **week 2** ingesteld. Dat hoef je hier niet opnieuw te doen.

> Je eigen repo heb je al in **week 2** gemaakt. Daar werk je in verder.

### 1. Basis-workflow (elke keer dat je werkt)

```bash
# 1. App starten
python app.py
# 2. Browser openen: http://127.0.0.1:5000
# 3. Basisdata laden: http://127.0.0.1:5000/laad-basisdata
# 4. Data bekijken:    http://127.0.0.1:5000/data
# 5. Stoppen: Ctrl+C
```

### 2. Handige commando's / snippets (SQLite + Flask)

| Actie | Code |
|---|---|
| Verbinding maken | `sqlite3.connect("data.db")` |
| Tabel aanmaken | `CREATE TABLE IF NOT EXISTS items (...)` |
| Rijen ophalen | `SELECT * FROM items` |
| Filteren | `SELECT * FROM items WHERE naam = ?` |
| Sorteren | `SELECT * FROM items ORDER BY naam` |
| Toevoegen | `INSERT INTO items (naam, beschrijving) VALUES (?, ?)` |
| Tellen | `SELECT COUNT(*) FROM items` |
| Route in Flask | `@app.route("/data")` |
| Route met GET/POST | `@app.route("/toevoegen", methods=["GET", "POST"])` |
| Formulier (HTML) | `<form method="POST" action="...">` |
| Veld ophalen | `request.form.get("naam")` |
| Redirect na opslaan | `redirect(url_for("data"))` |
| Template renderen | `render_template("data.html", items=items)` |

### 3. Veelgemaakte fouten (SQLite + Flask)

- **"no such table: items"** → Je hebt `init_db()` nog niet aangeroepen; start de app opnieuw.
- **"sqlite3.OperationalError: database is locked"** → Verbinding niet gesloten; gebruik `conn.close()` of een `with`-blok.
- **Geen data op de pagina** → Klik eerst op "Laad basisdata" (`/laad-basisdata`).
- **"TemplateNotFound"** → Het HTML-bestand staat niet in de map `templates/`.
- **CSS werkt niet** → Controleer het pad in `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`.
- **"Address already in use"** → Er draait al een app; stop de vorige met Ctrl+C.
- **"405 Method Not Allowed"** → De route ondersteunt geen POST; voeg `methods=["GET", "POST"]` toe.
- **Formulier doet niets** → Controleer `method="POST"` en `action="{{ url_for('toevoegen') }}"`.
- **Veld is leeg/None** → Gebruik `request.form.get("naam", "")` en valideer de invoer.

## Opdrachten (week 4)

- Maak een HTML-formulier (input + textarea + submit-knop) in een nieuwe pagina (`templates/toevoegen.html`).
- Maak een route die GET (formulier tonen) en POST (data opslaan) afhandelt (`/toevoegen`).
- Koppel het formulier aan de database: haal de velden op via `request.form` en voer `INSERT INTO` uit.
- Toon na opslaan de bijgewerkte lijst (redirect naar `/data`).
- Valideer de invoer (bijv. verplicht veld) en toon een foutmelding bij lege invoer.
- Lopen er dingen vast? Zet de taak op 'Showstopper' en neem dit mee naar het Daltonuur.

## Hulp

### Queries maken (SQL)

Je gebruikt SQL-queries om data op te halen of te wijzigen:
- `SELECT * FROM items` — alle rijen ophalen
- `SELECT * FROM items WHERE naam = '...'` — filteren
- `SELECT * FROM items ORDER BY naam` — sorteren
- `INSERT INTO items (naam, beschrijving) VALUES (?, ?)` — toevoegen (gebruik `?` voor veilige parameters)
- `SELECT COUNT(*) FROM items` — tellen

Kijk op W3Schools: **SQL** (https://www.w3schools.com/sql/) en **Python → SQLite** (https://www.w3schools.com/python/python_mysql_getstarted.asp).

### Hulp

- **sqlite3-module:** ingebouwd in Python, geen installatie nodig. Gebruik `conn.row_factory = sqlite3.Row` om kolommen als dict te benaderen.
- **Databasebestand:** het `.db`-bestand staat in je projectmap; zet het in `.gitignore` (staat al).
- **Flask & templates:** gebruik `render_template('data.html', items=items)` en een `{% for %}`-loop in de template.
- **Formulieren:** gebruik `<form method="POST">` en `request.form`; zie W3Schools **HTML Forms** (https://www.w3schools.com/html/html_forms.asp) en **Python → Flask** (https://www.w3schools.com/python/python_flask.asp).
- **Route testen:** start de app (`python app.py`) en open http://127.0.0.1:5000/toevoegen.

