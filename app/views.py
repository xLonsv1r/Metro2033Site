from app import app
from flask import render_template
import sqlite3


conn = sqlite3.connect("metro_database.db",check_same_thread=False) 
cursor = conn.cursor()

def get_all_guns():

    sql = "SELECT * FROM gun"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_all_stations():

    sql = "SELECT * FROM station"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_all_people():

    sql = "SELECT * FROM people"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_gun_by_id(gun_id):

    sql = "SELECT name FROM gun WHERE id = ?"
    cursor.execute(sql, (gun_id, ))
    result = cursor.fetchone()
    return  result


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/station")
def station():
    all_stations = get_all_stations()
    return render_template("public/station.html", all_stations=all_stations)

@app.route("/people")
def people():
    all_people = get_all_people()
    gun_id = all_people[0][3]
    gun_name = get_gun_by_id(gun_id)
    print(gun_name[0])
    return render_template("public/people.html", all_people=all_people,gun_name=gun_name[0])

@app.route("/guns")
def guns():
    all_guns = get_all_guns()

    return render_template("public/guns.html",all_guns=all_guns)
