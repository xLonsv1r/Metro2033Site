from app import app
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/station.html")

@app.route("/admin/dashboard/add")
def admin_dashboard2():
    return render_template("admin/dashboard.html")


@app.route("/admin/dashboard/guns")
def admin_guns():
    return render_template("admin/guns.html")


@app.route("/admin/dashboard/station")
def admin_station():
    return render_template("admin/station.html")


@app.route("/admin/dashboard/people")
def admin_people():
    return render_template("admin/people.html")

