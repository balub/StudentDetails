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
         print(students)
         return [
             {
                "name": students[0]['name'],
                "phNum": students[0]['phNum'],
                "email": students[0]['email'],
                "edu": students[0]['edu'],
                "college": students[0]['college'],
                "city": students[0]['city'],
                "state": students[0]['state'],
                "country": students[0]['country']
            },
             {
                 "name": students[1]['name'],
                 "phNum": students[1]['phNum'],
                 "email": students[1]['email'],
                 "edu": students[1]['edu'],
                 "college": students[1]['college'],
                 "city": students[1]['city'],
                 "state": students[1]['state'],
                 "country": students[1]['country']
             },
             {
                 "name": students[2]['name'],
                 "phNum": students[2]['phNum'],
                 "email": students[2]['email'],
                 "edu": students[2]['edu'],
                 "college": students[2]['college'],
                 "city": students[2]['city'],
                 "state": students[2]['state'],
                 "country": students[2]['country']
             }
         ]
         # for students in collection.find():
        #     all_students = []
        #     all_students.append({
        #         "name": students['name'],
        #         "phNum": students['phNum'],
        #         "email": students['email'],
        #         "edu": students['edu'],
        #         "college": students['college'],
        #         "city": students['city'],
        #         "state": students['state'],
        #         "country": students['country'],
        #         "size": collection.count()
        #     })
        #     return all_students


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
