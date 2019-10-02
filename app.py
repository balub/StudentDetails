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
        students = list(collection.find())
        all_students = []
        for student in students:
            all_students.append({
                "name": student['name'],
                "phNum": student['phNum'],
                "email": student['email'],
                "edu": student['edu'],
                "college": student['college'],
                "city": student['city'],
                "state": student['state'],
                "country": student['country']
            })
        return all_students


class Student(Resource):
    def get(self, name):
        student = collection.find({"name": name})
        for student in student:
            return {
                "name": student['name'],
                "phNum": student['phNum'],
                "email": student['email'],
                "edu": student['edu'],
                "college": student['college'],
                "city": student['city'],
                "state": student['state'],
                "country": student['country'],
                "size": collection.count()
            }


api.add_resource(AllStudents, '/students')
api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
