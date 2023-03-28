import os
from flask import Flask, request
import student
from flask_sqlalchemy import SQLAlchemy
import psycopg2


#basedir = os.path.abspath(os.path.dirname("C:\\Users\\muhannad ahmed\\Desktop\\Myproject\\transportation_main.py"))
app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:AsdMnb134@transportation-registration-dbEngine.cojapz86juvh.us-east-2.rds.amazonaws.com:5432/transportation_registration_DB'
dbEngine = SQLAlchemy(app)


class Student (dbEngine.Model):
    student_ID = dbEngine.Column(dbEngine.Integer, primary_key=True)
    first_name = dbEngine.Column (dbEngine.String(100), nullable=False)
    last_name = dbEngine.Column (dbEngine.String(100), nullable=False)
    level = dbEngine.Column (dbEngine.String(100), nullable=False)
    GAF_email = dbEngine.Column (dbEngine.String(80), unique=True, nullable=False)
    bus_route = dbEngine.Column (dbEngine.String(100), nullable=False)

   





@app.get("/test")
def test():
    return "hello world"

@app.get("/student/list")
def list_students():
    my_students_list = Student.query.all()
    return my_students_list

@app.get("/student/<student_id>")
def retrieve_student_by_id():
    my_student_id = request.args.get("student_id")
    return Student.query.filter(Student.student_ID == my_student_id).first()


@app.post("/student/new")
def create_student():
    student_ID = request.json.student_ID
    first_name = request.json.first_name
    last_name = request.json.last_name
    level = request.json.level
    GAF_email = request.json.GAF_email
    bus_route = request.json.bus_route

    my_student = Student(student_ID, first_name, last_name, level, GAF_email, bus_route)
    dbEngine.session.add(my_student)
    return dbEngine.session.commit()


@app.put("/student/update/<student_id>")
def update_student_by_id():
    selected_student = Student.query.filter(Student.student_ID == request.args.get("student_id")).one()

    student_ID = request.json.student_ID
    first_name = request.json.first_name
    last_name = request.json.last_name
    level = request.json.level
    GAF_email = request.json.GAF_email
    bus_route = request.json.bus_route

    selected_student.student_ID = student_ID
    selected_student.first_name = first_name
    selected_student.last_name = last_name
    selected_student.level = level
    selected_student.GAF_email = GAF_email
    selected_student.bus_route = bus_route


    dbEngine.session.update(selected_student)
    return dbEngine.session.commit()

@app.delete("/student/delete/<student_id>")
def delete_student_by_id():
    selected_student = Student.query.filter(Student.student_ID == request.args.get("student_id")).one()
    dbEngine.session.delete(selected_student)
    return dbEngine.session.commit()


