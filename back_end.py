import MySQLdb
from MySQLdb import cursors

import flask, json
from flask import request, redirect, url_for, jsonify
from flask import render_template
import pymysql

# link to database
DB_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'community_manager',
    'charset': 'utf8',
    'cursorclass': cursors.DictCursor
}

app = flask.Flask(__name__)

conn = MySQLdb.Connection(**DB_CONF)
cursor = conn.cursor()


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
        sql = 'UPDATE member_login SET login=1 WHERE Sno="{}"'.format(username)
        cursor.execute(sql)
        conn.commit()
        sql = 'SELECT * FROM member_login WHERE Sno = "{}" and Password = "{}"'.format(username, password)
        cursor.execute(sql)
        conn.commit()
        member_list = cursor.fetchall()
        if len(member_list) > 0:
            return redirect(url_for('home'))
    else:
        sql = 'UPDATE member_login SET login=1 WHERE Sno="{}"'.format(username)
        cursor.execute(sql)
        conn.commit()
        sql = 'SELECT * FROM member_login WHERE Sno = "{}" and Password = "{}"'.format(username, password)
        cursor.execute(sql)
        member_list = cursor.fetchall()
        if len(member_list) > 0:
            return redirect('/leader_home')
    return render_template("log_in.html")


@app.route("/home", methods=['POST', 'GET'])
def home():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    if len(username) > 0:
        sql = 'SELECT community FROM student WHERE Sno="{}"'.format(username.get('Sno'))
        cursor.execute(sql)
        conn.commit()
        com = cursor.fetchone()
        print(com)
        sql = 'SELECT * FROM community WHERE Cname="{}"'.format(com.get('community'))
        cursor.execute(sql)
        conn.commit()
        com_info = cursor.fetchone()
        print(com_info)
        if com_info is None:
            com_info = {'Cno': '', 'Cname': '', 'Ctype': '', 'Csno': '', 'Crank': '',
                        'Cdept': '', 'Cnum': '', 'Crno': '', 'Cdate': '',
                        'Cpass': '', 'Csname': ''}
        return render_template("home.html", **com_info)
    return render_template("home.html")


@app.route("/exit_com", methods=['POST', 'GET'])
def exit_com():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()
    sql = 'UPDATE community SET Cnum = Cnum - 1 where Cname="{}"'.format(com.get('community'))
    cursor.execute(sql)
    conn.commit()
    sql = 'UPDATE student SET community = NULL where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    print("success")
    return redirect("/home")


@app.route("/club_lists", methods=['POST', 'GET'])
def club_lists():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Cno, Cname FROM community'
    cursor.execute(sql)
    conn.commit()
    clublists = cursor.fetchall()
    print(clublists)
    return render_template("club_lists.html", clublists=clublists)


@app.route("/join_in", methods=['POST', 'GET'])
def join_in():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    Sno = cursor.fetchone()
    print(Sno)
    cno = request.form.get("Cno")
    cname = request.form.get("Cname")
    print(cno)
    print(cname)
    sql = 'UPDATE community SET Cnum = Cnum + 1 where Cname="{}"'.format(cname)
    cursor.execute(sql)
    conn.commit()
    sql = 'UPDATE student SET community = "{}" where Sno="{}"'.format(cname, Sno.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    print("success")
    sql = 'SELECT Cno, Cname FROM community'
    cursor.execute(sql)
    conn.commit()
    clublists = cursor.fetchall()
    print(clublists)
    return render_template("club_lists.html", clublists=clublists)


@app.route("/club_members", methods=['POST', 'GET'])
def club_members():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()
    sql = 'SELECT Sname, Sno, Sdept FROM student where community="{}"'.format(com.get('community'))
    cursor.execute(sql)
    conn.commit()
    member = cursor.fetchall()
    print(member)
    return render_template("club_members.html", member=member)


@app.route("/personal_info", methods=['POST', 'GET'])
def personal_info():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    sql = 'SELECT * FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    stu = cursor.fetchone()
    print(stu)
    return render_template("personal_info.html", stu=stu)


@app.route("/change_info", methods=['POST', 'GET'])
def change_info():
    if request.method == "GET":
        return render_template("change_perinfo.html")
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    sql = 'SELECT * FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    stu = cursor.fetchone()
    print(stu)
    print(request.form)
    Sno = request.form.get("sno")
    Sdept = request.form.get("dept")
    community = request.form.get("com")
    Wechat = request.form.get("wechat")
    Tel = request.form.get("phone")
    sql = 'UPDATE student SET Sdept="{}", community = "{}", Wechat = "{}", Tel = "{}" where Sno = "{}"'.format(Sdept, community, Wechat, Tel, Sno)
    cursor.execute(sql)
    conn.commit()
    print("success")


@app.route("/leader_home", methods=['POST', 'GET'])
def leader_home():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    if len(username) > 0:
        sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sno'))
        cursor.execute(sql)
        conn.commit()
        com = cursor.fetchone()
        print(com)
        sql = 'SELECT * FROM community where Cname="{}"'.format(com.get('community'))
        cursor.execute(sql)
        conn.commit()
        com_info = cursor.fetchone()
        print(com_info)
        if com_info is None:
            com_info = {'Cno': '', 'Cname': '', 'Ctype': '', 'Csno': '', 'Crank': '',
                        'Cdept': '', 'Cnum': '', 'Crno': '', 'Cdate': '',
                        'Cpass': '', 'Csname': ''}
        return render_template("leader_home.html", **com_info)
    return render_template("leader_home.html")


@app.route("/leader_exit_com", methods=['POST', 'GET'])
def leader_exit_com():

    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()

    sql = 'SELECT community FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()

    sql = 'UPDATE community SET Cnum = Cnum - 1 where Cname="{}"'.format(com.get('community'))
    cursor.excute(sql)
    conn.commit()

    sql = 'UPDATE student SET community = NULL where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    print("success")


@app.route("/leader_club_lists", methods=['POST', 'GET'])
def leader_club_lists():

    sql ='CREATE OR REPLACE VIEW V_clubs(Cno,Cname) AS SELECT Cno,Cname FROM community'
    cursor.execute(sql)
    conn.commit()

    sql = 'SELECT Cno, Cname FROM V_clubs'
    cursor.execute(sql)
    conn.commit()
    clublists = cursor.fetchall()
    print(clublists)

    return render_template("leader_club_lists.html", clublists=clublists)


@app.route("/leader_club_members", methods=['POST', 'GET'])
def leader_club_members():
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()

    sql = 'CREATE OR REPLACE VIEW leader_view_members(Sno,Sname,Sdept,Tel,community) AS SELECT Sno,Sname,Sdept,Tel,community FROM student'
    cursor.execute(sql)
    conn.commit()

    sql = 'SELECT community FROM leader_view_members where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()

    sql = 'SELECT Sname, Sno, Sdept,Tel FROM leader_view_members where community="{}"'.format(com.get('community'))
    cursor.execute(sql)
    conn.commit()
    member_list = cursor.fetchall()
    print(member_list)

    return render_template("leader_club_members.html", member_list=member_list)


@app.route("/leader_change_clubinfo", methods=['POST', 'GET'])
def leader_change_clubinfo():
    if request.method == "GET":
        return render_template("leader_change_clubinfo.html")
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    Cno = request.form.get("Cno")
    Cname = request.form.get("Cname")
    Ctype = request.form.get("Ctype")
    Crank = request.form.get("Crank")
    Crno = request.form.get("Crno")
    print(Cname)
    print(Ctype)
    sql = 'UPDATE community SET Cname="{}", Ctype = "{}", Crank = "{}", Crno = "{}" where Cno = "{}"'.format(Cname, Ctype, Crank, Crno, Cno)
    cursor.execute(sql)
    conn.commit()
    print("success")


@app.route("/leader_remove_members", methods=['POST', 'GET'])
def leader_remove_members():
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()

    Sname = request.form.get("Sname")
    Sno = request.form.get("Sno")
    Sdept = request.form.get("Sdept")
    Tel = request.form.get("Tel")
    print(Sname)
    print(Sno)
    print(Sdept)
    print(Tel)

    sql = 'SELECT Scno FROM student where Sno="{}"'.format(Sno)
    cursor.execute(sql)
    conn.commit()
    com = cursor.fetchone()
    print(com)

    sql = 'UPDATE student SET community=NULL WHERE Sno="{}"'.format(Sno)
    cursor.execute(sql)
    conn.commit()
    print('success')
    sql = 'UPDATE community SET Cnum=Cnum-1 WHERE Cno="{}"'.format(com.get('Scno'))
    cursor.execute(sql)
    conn.commit()

    sql = 'SELECT Sname,Sno,Sdept,Tel FROM student WHERE Scno="{}"'.format(com.get('Scno'))
    cursor.execute(sql)
    conn.commit()
    member_list = cursor.fetchall()
    print(member_list)
    return render_template("leader_club_members.html", member_list=member_list)


@app.route("/leader_personal_info", methods=['POST', 'GET'])
def leader_personal_info():
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)

    if len(username) > 0:
        sql = 'SELECT Sno, Sname, Ssex, Sdept, community, Status, Wechat, Tel FROM student where Sno="{}"'.format(username.get('Sno'))
        cursor.execute(sql)
        conn.commit()
        person_info = cursor.fetchone()
        print(person_info)
        return render_template("leader_personal_info.html", **person_info)
    return render_template("leader_personal_info.html")


@app.route("/leader_change_perinfo", methods=['POST', 'GET'])
def leader_change_perinfo():
    if request.method == "GET":
        return render_template("leader_change_perinfo.html")
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    sql = 'SELECT Sno FROM member_login WHERE login=1'
    cursor.execute(sql)
    conn.commit()
    username = cursor.fetchone()
    print(username)
    sql = 'SELECT * FROM student where Sno="{}"'.format(username.get('Sno'))
    cursor.execute(sql)
    conn.commit()
    stu = cursor.fetchone()
    print(stu)
    print(request.form)
    Sno = request.form.get("sno")
    Sdept = request.form.get("dept")
    community = request.form.get("com")
    Wechat = request.form.get("wechat")
    Tel = request.form.get("phone")
    sql = 'UPDATE student SET Sdept="{}", community = "{}", Wechat = "{}", Tel = "{}" where Sno = "{}"'.format(Sdept, community, Wechat, Tel, Sno)
    cursor.execute(sql)
    conn.commit()
    print("success")

@app.route("/leader_add_member", methods=['POST', 'GET'])
def leader_add_member():
    if request.method == "GET":
        return render_template("leader_add_member.html")
    conn = MySQLdb.Connection(**DB_CONF)
    cursor = conn.cursor()
    print(request.form)
    Sname = request.form.get("name")
    Sno = request.form.get("sno")
    Sdept = request.form.get("dept")
    Ssex = request.form.get("sex")
    Password = request.form.get("pwd")
    community = request.form.get("com")
    Wechat = request.form.get("wechat")
    Tel = request.form.get("phone")
    sql = 'SELECT Cno FROM community where Cname = "{}"'.format(community)
    cursor.execute(sql)
    conn.commit()
    Scno = cursor.fetchone().get('Cno')
    sql = 'INSERT INTO student values("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(Sno, Sname, Ssex, Sdept, Scno, community, 'member', Wechat, Tel)
    cursor.execute(sql)
    conn.commit()
    sql = 'INSERT INTO member_login values("{}", "{}", "{}")'.format(Sno, Password, 0)
    cursor.execute(sql)
    conn.commit()
    sql = 'UPDATE community SET Cnum = Cnum + 1 where Cno ="{}"'.format(Scno)
    cursor.execute(sql)
    conn.commit()
    print("success")


if __name__ == "__main__":
    app.run(debug=True)
