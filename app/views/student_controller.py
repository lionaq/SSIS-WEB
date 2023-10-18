from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, redirect, url_for
from app.Models import studentModel, courseModel

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    result = studentModel.all()
    courseCode = courseModel.all()
    print(courseCode)
    courses = [item for item in courseCode]
    print(result)
    error = request.args.get('error')
    success = request.args.get('success')
    return render_template('student.html', data = result, courses = courses, error = error, success = success)

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
        try:
            studentModel.insert(list)
            return redirect (url_for('student.data', success = True))
        except: 
            return redirect (url_for('student.data', error = True))

