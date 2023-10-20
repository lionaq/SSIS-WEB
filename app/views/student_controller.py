from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.Models import studentModel, courseModel

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    result = studentModel.all()
    courseCode = courseModel.all()
    print(courseCode)
    courses = [item for item in courseCode]
    print(result)
    return render_template('student.html', data = result, courses = courses)

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
            flash(f"Student {studentId} Added Successfully!", "info")
            return redirect (url_for('student.data'))
        except:
            flash(f"Student ID '{studentId}' already exists!", "error") 
            return redirect (url_for('student.data'))

@student.route('/student/update', methods = ['POST'])
def update():
    if request.method == "POST":

        idOne = request.form['idOne_edit']
        idTwo = request.form['idTwo_edit']
        studentId = idOne + '-' + idTwo
        first_name = request.form['first_name_edit']
        last_name = request.form['last_name_edit']
        course_code = request.form['course_code_edit']
        year_level = request.form['year_level_edit']
        gender = request.form['gender_edit']

        list = [ first_name, last_name, course_code, year_level, gender, studentId]
        print(list)
        try:
            studentModel.update(list)
            return redirect (url_for('student.data'))
        except: 
            return redirect (url_for('student.data'))
        
@student.route('/student/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        data = (id,)
        studentModel.delete(data)
        flash(f"Student {id} Deleted Successfully!", "info")
        return redirect(url_for('student.data'))