from flask import Flask, render_template, redirect, request, url_for, jsonify,json
from flask_restful import Resource, Api
import psycopg2
app = Flask(__name__)
api = Api(app)

class movies(Resource):
    def get(self):
        connection=psycopg2.connect("host='moviesDB' dbname='movies' user='postgres' password='postgres'")
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM movies")
        rows=cursor.fetchall()
        cursor.close()
        connection.close()
        test=jsonify(rows)
        return test
api.add_resource(movies,'/movies')


