import pymongo
import flask
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0-hz7um.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["StudentDetails"]
collection = db["students"]

app = Flask(__name__)
api = Api(app)


class AllStudents(Resource):
    def get(self):
        students = collection.find({})
        return {'students': collection.count()}


api.add_resource(AllStudents, '/students')

app.run(port=5000)
