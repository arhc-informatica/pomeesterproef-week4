from flask import Flask, render_template, redirect, url_for, request
import database

app = Flask(__name__)

database.init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/laad-basisdata")
def laad_basisdata():
    database.laad_basisdata()
    return redirect(url_for("data"))


@app.route("/data")
def data():
    items = database.get_items()
    return render_template("data.html", items=items)


@app.route("/toevoegen", methods=["GET", "POST"])
def toevoegen():
    """Formulier om een nieuwe rij toe te voegen (koppeling form -> database)."""
    if request.method == "POST":
        naam = request.form.get("naam", "").strip()
        beschrijving = request.form.get("beschrijving", "").strip()
        if naam:
            database.voeg_item_toe(naam, beschrijving)
        return redirect(url_for("data"))
    return render_template("toevoegen.html")


if __name__ == "__main__":
    app.run(debug=True)