from flask import Blueprint, render_template, request, redirect, url_for
from app.Models import studentModel

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    result = studentModel.all()
    print(result)
    return render_template('student.html', data = result)

@student.route('/student/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        idOne = request.form['idOne']
        idTwo = request.form['idTwo']
        studentId = idOne + '-' + idTwo
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        course_code = request.form['course_code']
        year_level = request.form['year_level']
        gender = request.form['gender']

        list = [studentId, first_name, last_name, course_code, year_level, gender]
        print(list)
        studentModel.insert(list)
        return redirect (url_for('student.data'))

