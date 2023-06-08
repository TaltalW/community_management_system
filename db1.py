import MySQLdb
from MySQLdb import cursors

import flask, json
from flask import request, redirect, url_for, jsonify
from flask import render_template
import pymysql
#link to database
DB_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'Tal@029118',
    'db': 'commynity',
    'charset': 'utf8',
    'cursorclass': cursors.DictCursor
}
user = ""
user_status = ""

app = flask.Flask(__name__)

@app.route("/log_in", methods=['POST', 'GET'])
def log_in():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    # get infomation from the form
    username = request.args.get('username')
    password = request.args.get("pwd")
    status = request.args.getlist("status")
    print(password)
    print(status)
    if status == ['member']:
        sql = 'SELECT * FROM member_login WHERE Sname = "{}" and Password = "{}"'.format(username, password)
        cursor.execute(sql)
        conn.commit()
        member_list = cursor.fetchall()
        if len(member_list) > 0:
            return redirect(url_for('home'))
    else:
        sql = 'SELECT * FROM communaty_login WHERE Cname = "{}" and Cpass = "{}"'.format(username, password)
        cursor.execute(sql)
        member_list = cursor.fetchall()
        if len(member_list) > 0:
            return redirect('/home')
    return render_template("log_in.html")

@app.route("/home", methods=['POST', 'GET'])
def home():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sname FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    if len(username) > 0:
        sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sname'))
        cursor.execute(sql)
        conn.commit()
        com = cursor.fetchone()
        print(com)
        sql = 'SELECT * FROM communaty where Cname="{}"'.format(com.get('community'))
        cursor.execute(sql)
        conn.commit()
        com_info = cursor.fetchone()
        print(com_info)
        return render_template("home.html", **com_info)
    return render_template("home.html")
@app.route("/exit_com", methods=['POST', 'GET'])
def exit_com():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sname FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sname'))
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()
    sql = 'UPDATE communaty SET Cnum = Cnum - 1 where where Cname="{}"'.format(com.get('community'))
    cursor.excute(sql)
    conn.commit()
    sql = 'UPDATE student SET community = NULL where Sno="{}"'.format(username.get('Sname'))
    cursor.execute(sql)
    conn.commit()
    print("success")

@app.route("/club_lists", methods=['POST', 'GET'])
def club_lists():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Cno, Cname FROM communaty'
    cursor.execute(sql)
    conn.commit()
    clublists = cursor.fetchall()
    print(clublists)
    return render_template("club_lists.html", clublists=clublists)

if __name__== "__main__":
    app.run(debug=True)