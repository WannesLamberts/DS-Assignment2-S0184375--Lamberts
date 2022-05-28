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
            connection = psycopg2.connect("host='localhost' dbname='users' user='postgres' password='123456'")
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
        connection = psycopg2.connect("host='localhost' dbname='users' user='postgres' password='123456'")
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
            connection = psycopg2.connect("host='localhost' dbname='users' user='postgres' password='123456'")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO friends(userfrom,userto) VALUES(%s,%s) ", (username,fusername))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            return False


api.add_resource(register,'/register')
api.add_resource(login,'/login')
api.add_resource(addfriend,'/addfriend')


