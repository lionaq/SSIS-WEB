from flask import Blueprint, render_template, request, redirect, url_for, flash
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
            flash(f"Course {courseCode.upper()} Added Successfully!", "info")
            return redirect (url_for('course.data'))
        except:
            flash(f"Course {courseCode.upper()} Already Exists!", "error")
            return redirect (url_for('course.data'))

@course.route('/course/update/', methods = ['POST'])
def update():
    if request.method == "POST":
        initCourseCode = request.form['initCourseCode']
        course_code = request.form['course_code_edit']
        course_edit = request.form['course_edit']
        college_code_edit = request.form['college_code_edit']

        list = [course_code.upper(), course_edit.title(), college_code_edit, initCourseCode]
        print(list)
        try:
            courseModel.update(list)
            flash(f"Course {initCourseCode.upper()} Edited Successfully!", "info")
            return redirect (url_for('course.data'))
        except:
            flash(f"Course {course_code.upper()} Already Exists! Cannot Edit Current Course To Existing Course.", "info")
            return redirect (url_for('course.data'))
        
@course.route('/course/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        data = (id,)
        courseModel.delete(data)
        flash(f"Course {id} Deleted Successfully!", "info")
        return redirect(url_for('course.data'))