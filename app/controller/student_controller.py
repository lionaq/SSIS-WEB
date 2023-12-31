from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.Models import studentModel, courseModel
from cloudinary import uploader
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    result = studentModel.all()
    courseCode = courseModel.all()
    courses = [item for item in courseCode]
    return render_template('student.html', data = result, courses = courses)

@student.route('/student/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        studentPic = request.files['studentPic']
        idOne = request.form['idOne']
        idTwo = request.form['idTwo']
        studentId = idOne + '-' + idTwo
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        course_code = request.form['course_code']
        year_level = request.form['year_level']
        gender = request.form['gender']
        try:
            if studentPic:
                upload_result = upload(studentPic, folder="SSIS", resource_type='image')
                secure_url = upload_result['secure_url']
            else:
                secure_url = None
                
            list = [secure_url,studentId, first_name, last_name, course_code, year_level, gender]
            studentModel.insert(list)
            print('PIC IS:',secure_url)
            flash(f"Student {studentId} Added Successfully!", "info")
            return redirect (url_for('student.data'))
        except:
            flash(f"Student ID '{studentId}' already exists!", "error") 
            return redirect (url_for('student.data'))

@student.route('/student/update', methods = ['POST'])
def update():
    if request.method == "POST":
        studentPicEdit = request.files['studentPicEdit']
        idOne = request.form['idOne_edit']
        idTwo = request.form['idTwo_edit']
        studentId = idOne + '-' + idTwo
        first_name = request.form['first_name_edit']
        last_name = request.form['last_name_edit']
        course_code = request.form['course_code_edit']
        year_level = request.form['year_level_edit']
        gender = request.form['gender_edit']

        initIdOne = request.form['initIdEditOne']
        initIdTwo = request.form['initIdEditTwo']

        initStudentId = initIdOne + '-' + initIdTwo

        list = [studentId, first_name, last_name, course_code, year_level, gender, initStudentId]
        print(list)
        try:  
            studentModel.update(list)
            if studentPicEdit:
                print("IMIN")
                oldPic = studentModel.fetchProfilePic([studentId])
                print(oldPic[0]['student_pic'])
                if oldPic[0]['student_pic'] != None:
                    print("WHY")
                    public_id = studentModel.getPublicId(oldPic[0]['student_pic'])
                    print(public_id)
                    delete = uploader.destroy(public_id)
                    print(delete, " ", oldPic[0]['student_pic'], "DELETED")

                result = upload(studentPicEdit, folder="SSIS", resource_type='image')
                secure_url = result['secure_url']
                studentModel.updateProfilePic([secure_url, studentId])

            flash(f"Student {initStudentId} Edited Successfully!", "info")
            return redirect (url_for('student.data'))
        except: 
            flash(f"Student {studentId} Already Exists! Cannot Edit Current Student To Existing Student.", "error")
            return redirect (url_for('student.data'))
        
@student.route('/student/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        try:
            oldPic = studentModel.fetchProfilePic([id])
            if oldPic[0]['student_pic'] != None:
                public_id = studentModel.getPublicId(oldPic[0]['student_pic'])
                delete = uploader.destroy(public_id)
                print(delete, " ", oldPic[0]['student_pic'], "DELETED")

            data = (id,)
            studentModel.delete(data)
            flash(f"Student {id} Deleted Successfully!", "info")
            return redirect(url_for('student.data'))
        
        except:
            flash(f"Student {id} Deletion Failed!", "error")
            return redirect(url_for('student.data'))