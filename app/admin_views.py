from app import app
from flask import render_template, request
import sqlite3

admin_conn = sqlite3.connect("metro_database.db",check_same_thread=False) 
admin_cursor = admin_conn.cursor()

def add_new_gun(name, bullet_count, description, photo_name):
    sql_query = """ INSERT INTO gun
                (name, bullet_count, description, photo_path) 
                VALUES(?, ?, ?, ?); """
    data_turple = (name, bullet_count, description, "static/img/"+photo_name)
    admin_cursor.execute(sql_query, data_turple)
    admin_conn.commit()

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


@app.route("/admin/dashboard/guns/add", methods=['post','get'])
def admin_add_gun():
    if request.method == "POST":
        name = request.form.get('inputGunName')
        bullet_count = request.form.get('inputBulletCount')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        add_new_gun(name, bullet_count, description, photo_name)

    return render_template("admin/add_gun.html")

@app.route("/admin/dashboard/station/add")
def admin_add_station():
    return "station form"

@app.route("/admin/dashboard/people/add")
def admin_add_people():
    return "people form"