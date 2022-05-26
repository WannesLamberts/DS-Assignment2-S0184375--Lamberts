from flask import Flask, render_template, redirect, request, url_for, jsonify,json
from flask_restful import Resource, Api
import psycopg2
app = Flask(__name__)
api = Api(app)

class movies(Resource):
    def get(self):
        connection=psycopg2.connect("host='localhost' dbname='movies' user='postgres' password='123456'")
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM movies')
        rows=cursor.fetchall()
        print("test")
        test=jsonify(rows)
        return test
api.add_resource(movies,'/movies')
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

