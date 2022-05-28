from flask import Flask, render_template, redirect, request, url_for, jsonify,json
from flask_restful import Resource, Api
import psycopg2
app = Flask(__name__)
api = Api(app)

class register(Resource):
    def post(self):
        try:
            data=request.json
            username=data["username"]
            password=data["password"]
            connection = psycopg2.connect("host='usersDB' dbname='users' user='postgres' password='postgres'")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users(username,password) VALUES(%s,%s)",(username,password))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            return False
class login(Resource):
    def get(self):
        data = request.json
        username = data["username"]
        password = data["password"]
        connection = psycopg2.connect("host='usersDB' dbname='users' user='postgres' password='postgres'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username= %s ",(username,))
        record = cursor.fetchone()
        cursor.close()
        connection.close()
        if record==None:
            return False
        if record[1]!=password:
            return False
        return True
class addfriend(Resource):
    def post(self):
        try:
            data = request.json
            username = data["username"]
            fusername = data["fusername"]
            connection = psycopg2.connect("host='usersDB' dbname='users' user='postgres' password='postgres'")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO friends(userfrom,userto) VALUES(%s,%s) ", (username,fusername))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            return False
class creategroup(Resource):
    def post(self):
        try:
            data = request.json
            groupename = data["groupname"]
            username = data["username"]
            connection = psycopg2.connect("host='usersDB' dbname='users' user='postgres' password='postgres'")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO groups(groupname,creator) VALUES(%s,%s) ", (groupename, username))
            cursor.execute("INSERT INTO groupmembers(groupname,member) VALUES(%s,%s) ", (groupename, username))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            return False
class addtogroup(Resource):
    def post(self):
        data = request.json
        groupename = data["groupname"]
        username = data["username"]
        friendname = data["friendname"]
        connection = psycopg2.connect("host='usersDB' dbname='users' user='postgres' password='postgres'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM friends WHERE userfrom= %s AND userto= %s",(username,friendname))
        record=cursor.fetchone()
        if(record==None):
            return False
        cursor.execute("SELECT * FROM groups WHERE groupname= %s",(groupename,))
        record=cursor.fetchone()
        if (record == None):
            return False
        cursor.execute("SELECT * FROM groupmembers WHERE groupname= %s AND member=%s",(groupename,username))
        record=cursor.fetchone()
        if (record == None):
            return False
        cursor.execute("INSERT INTO groupmembers(groupname,member) VALUES(%s,%s) ", (groupename, friendname))
        connection.commit()
        cursor.close()
        connection.close()
        return True



api.add_resource(register,'/register')
api.add_resource(login,'/login')
api.add_resource(addfriend,'/addfriend')
api.add_resource(creategroup,'/creategroup')
api.add_resource(addtogroup,'/addtogroup')



