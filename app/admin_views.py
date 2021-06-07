from app import app
from flask import render_template, request
import sqlite3


admin_conn = sqlite3.connect("metro_database.db",check_same_thread=False) 
admin_cursor = admin_conn.cursor()

def update_gun(task):
    sql_update_query = """ UPDATE gun
                            SET name = ?, 
                                bullet_count = ?, 
                                description = ?,
                                photo_path = ?
                            WHERE id = ?
                        """

    admin_cursor.execute(sql_update_query, task)
    admin_conn.commit()

def update_station(task):
    sql_update_query = """ UPDATE station
                            SET name = ?, 
                                people_count = ?, 
                                status = ?,
                                description = ?,
                                photo_path = ?
                            WHERE id = ?
                        """

    admin_cursor.execute(sql_update_query, task)
    admin_conn.commit()


def update_people(task):
    sql_update_query = """ UPDATE people
                            SET name = ?, 
                                id_station = ?, 
                                id_gun = ?,
                                description = ?,
                                photo_path = ?
                            WHERE id = ?
                        """

    admin_cursor.execute(sql_update_query, task)
    admin_conn.commit()



def delete_gun_by_id(id):
    sql_delete_query = """ DELETE from gun where id = ?"""
    admin_cursor.execute(sql_delete_query, (id, ))
    admin_conn.commit()

def delete_people_by_id(id):
    sql_delete_query = """ DELETE from people where id = ?"""
    admin_cursor.execute(sql_delete_query, (id, ))
    admin_conn.commit()

def delete_station_by_id(id):
    sql_delete_query = """ DELETE from station where id = ?"""
    admin_cursor.execute(sql_delete_query, (id, ))
    admin_conn.commit()



def get_all_guns():

    sql = "SELECT * FROM gun"
    admin_cursor.execute(sql)
    result = admin_cursor.fetchall()
    return result

def get_all_stations():
    sql = "SELECT * FROM station"
    admin_cursor.execute(sql)
    result = admin_cursor.fetchall()
    return result

def get_all_people():
    sql = "SELECT * FROM people"
    admin_cursor.execute(sql)
    result = admin_cursor.fetchall()
    return result



def add_new_gun(name, bullet_count, description, photo_name):
    sql_query = """ INSERT INTO gun
                (name, bullet_count, description, photo_path) 
                VALUES(?, ?, ?, ?); """
    data_turple = (name, bullet_count, description, "static/img/"+photo_name)
    admin_cursor.execute(sql_query, data_turple)
    admin_conn.commit()

def add_new_station(name,people_count, open_data, status, description, photo_name):
    sql_query = """ INSERT INTO station
                (name, people_count, open_data, status,description, photo_path) 
                VALUES(?, ?, ?, ?, ?, ?); """
    data_turple = (name, people_count, open_data, status, description, "static/img/"+photo_name)
    admin_cursor.execute(sql_query, data_turple)
    admin_conn.commit()

def add_new_people(name, id_station, id_gun, birthday_date, description, photo_name):
    sql_query = """ INSERT INTO people
                (name, id_station, id_gun, birthday_date, description, photo_path) 
                VALUES(?, ?, ?, ?, ?, ?); """
    data_turple = (name, id_station, id_gun, birthday_date, description, "static/img/"+photo_name)
    admin_cursor.execute(sql_query, data_turple)
    admin_conn.commit()



@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/station.html")



@app.route("/admin/dashboard/guns", methods=['post','get'])
def admin_guns():
    if request.method == "POST":
        if request.form['delete']:
            delete_gun_by_id(request.form['delete'])

    all_guns = get_all_guns()
    return render_template("admin/guns.html", all_guns = all_guns)


@app.route("/admin/dashboard/station", methods=['post', 'get'])
def admin_station():
    if request.method == "POST":
        if request.form['delete']:
            delete_station_by_id(request.form['delete'])

    all_stations = get_all_stations()
    return render_template("admin/station.html", all_stations=all_stations)


@app.route("/admin/dashboard/people", methods=['post', 'get'])
def admin_people():
    if request.method == "POST":
        if request.form['delete']:
            delete_people_by_id(request.form['delete'])

    all_people = get_all_people()
    return render_template("admin/people.html", all_people=all_people)


@app.route("/admin/dashboard/guns/add", methods=['post','get'])
def admin_add_gun():
    if request.method == "POST":
        name = request.form.get('inputGunName')
        bullet_count = request.form.get('inputBulletCount')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        add_new_gun(name, bullet_count, description, photo_name)

    return render_template("admin/add_gun.html")

@app.route("/admin/dashboard/station/add", methods=['post','get'])
def admin_add_station():
    if request.method == "POST":
        name = request.form.get('inputStationName')
        people_count = request.form.get('inputPeopleCount')
        open_data = request.form.get('inputDate')
        status = request.form.get('inputStatus')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        add_new_station(name, people_count,open_data,status, description, photo_name)

    return render_template("admin/add_station.html")



@app.route("/admin/dashboard/people/add", methods=['post','get'])
def admin_add_people():
    if request.method == "POST":
        name = request.form.get('inputPersonName')
        id_station = request.form.get('inputIdStation')
        id_gun = request.form.get('inputIdGun')
        birthday_date = request.form.get('inputBirthdayDate')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        
        add_new_people(name, id_station, id_gun, birthday_date, description, photo_name)

    return render_template("admin/add_people.html")


@app.route("/admin/dashboard/guns/update", methods=['post','get'])
def admin_update_gun():
    if request.method == "POST":
        name = request.form.get('inputGunName')
        bullet_count = request.form.get('inputBulletCount')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        id_gun = request.form['update']
        update_gun((name, bullet_count, description, photo_name, id_gun))


    all_guns = get_all_guns()
    return render_template("admin/update_gun.html", all_guns = all_guns)


@app.route("/admin/dashboard/station/update", methods=['post','get'])
def admin_update_station():
    if request.method == "POST":
        name = request.form.get('inputStationName')
        people_count = request.form.get('inputPeopleCount')
        status = request.form.get('inputStatus')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        id_station = request.form['update']
        update_station((name,people_count,status,description,photo_name,id_station))


    all_stations = get_all_stations()
    print(all_stations)
    return render_template("admin/update_station.html", all_stations = all_stations)


@app.route("/admin/dashboard/people/update", methods=['post','get'])
def admin_update_people():
    if request.method == "POST":
        name = request.form.get('inputPeopleName')
        id_station = request.form.get('inputIdStation')
        id_gun = request.form.get('inputIdGun')
        description = request.form.get('inputDescription')
        photo_name = request.form.get('inputPhotoName')
        id_people = request.form['update']
        update_people((name, id_station, id_gun, description, photo_name, id_people))


    all_people = get_all_people()
    return render_template("admin/update_people.html", all_people = all_people)

