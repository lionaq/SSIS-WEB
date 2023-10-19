from flask import Blueprint, render_template, request, redirect, url_for
from app.Models import courseModel

course = Blueprint('course', __name__)

@course.route('/course')
def data():
    result = courseModel.all()
    print(result)
    return render_template('course.html', data = result)

@course.route('/course/insert', methods = ['POST'])
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
            courseModel.insert(list)
            return redirect (url_for('course.data', success = True))
        except: 
            return redirect (url_for('course.data', error = True))

@course.route('/course/update', methods = ['POST'])
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
            courseModel.update(list)
            return redirect (url_for('course.data', success = True))
        except: 
            return redirect (url_for('course.data', error = True))
        
@course.route('/course/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        data = (id,)
        courseModel.delete(data)
        return redirect(url_for('course.data', success=True))