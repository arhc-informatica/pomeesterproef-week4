import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")


def get_connection():
    """Maak een verbinding met de SQLite-database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # zodat kolommen als dict benaderbaar zijn
    return conn


def init_db():
    """Maak de tabel aan als die nog niet bestaat."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            beschrijving TEXT
        )
    """)
    conn.commit()
    conn.close()


def laad_basisdata():
    """Laad een aantal basis-rijen in de tabel (alleen als tabel leeg is)."""
    conn = get_connection()
    cur = conn.execute("SELECT COUNT(*) FROM items")
    aantal = cur.fetchone()[0]
    if aantal == 0:
        basis = [
            ("Voorbeeld item 1", "Dit is een eerste voorbeeldrij."),
            ("Voorbeeld item 2", "Dit is een tweede voorbeeldrij."),
            ("Voorbeeld item 3", "Dit is een derde voorbeeldrij."),
            ("Voorbeeld item 4", "Dit is een vierde voorbeeldrij."),
            ("Voorbeeld item 5", "Dit is een vijfde voorbeeldrij."),
            ("Voorbeeld item 6", "Dit is een zesde voorbeeldrij."),
            ("Voorbeeld item 7", "Dit is een zevende voorbeeldrij."),
            ("Voorbeeld item 8", "Dit is een achtste voorbeeldrij."),
            ("Voorbeeld item 9", "Dit is een negende voorbeeldrij."),
            ("Voorbeeld item 10", "Dit is een tiende voorbeeldrij."),
        ]
        conn.executemany("INSERT INTO items (naam, beschrijving) VALUES (?, ?)", basis)
        conn.commit()
    conn.close()


def get_items():
    """Haal alle rijen op uit de tabel (SELECT *)."""
    conn = get_connection()
    rows = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return rows


def voeg_item_toe(naam, beschrijving):
    """Voeg een nieuwe rij toe (INSERT INTO)."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO items (naam, beschrijving) VALUES (?, ?)",
        (naam, beschrijving),
    )
    conn.commit()
    conn.close()