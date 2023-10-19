from flask import Blueprint, render_template, request, redirect, url_for
from app.Models import courseModel, collegeModel

course = Blueprint('course', __name__)

@course.route('/course')
def data():
    result = courseModel.all()
    college = collegeModel.all()
    print(result)
    return render_template('course.html', data = result, college = college)

@course.route('/course/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        courseCode = request.form['course_code']
        course = request.form['course']
        collegeCode = request.form['college_code']

        list = [courseCode.upper(), course, collegeCode]

        print(list)
        try:
            courseModel.insert(list)
            return redirect (url_for('course.data', success = True))
        except: 
            return redirect (url_for('course.data', error = True))

@course.route('/course/update', methods = ['POST'])
def update():
    if request.method == "POST":

        college_code = request.form['course_code_edit']
        course_edit = request.form['course_edit']
        college_code_edit = request.form['college_code_edit']

        list = [course_edit, college_code_edit, college_code]
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