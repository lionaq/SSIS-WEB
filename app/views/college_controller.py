from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.Models import collegeModel

college = Blueprint('college', __name__)


@college.route('/college')
def data():
    result = collegeModel.all()
    print(result)
    return render_template('college.html', data = result)


@college.route('/college/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        collegeCode = request.form['college_code']
        name = request.form['name']

        list = [collegeCode.upper(), name.title()]

        print(list)
        try:
            collegeModel.insert(list)
            flash(f"College {collegeCode.upper()} Added Successfully!", "info")
            return redirect (url_for('college.data'))
        except:
            flash(f"College {collegeCode.upper()} Already Exists!", "error")
            return redirect (url_for('college.data'))


@college.route('/college/update', methods = ['POST'])
def update():
    if request.method == "POST":

        collegeCode = request.form['college_code_edit']
        name_edit = request.form['name_edit']
        initCollegeCode = request.form['initCollegeCode']
        print(initCollegeCode)
        list = [collegeCode.upper(), name_edit.title(), initCollegeCode.upper()]
        print(list)
        try:
            flash(f"College {collegeCode.upper()} Edited Successfully!", "info")
            collegeModel.update(list)
            return redirect (url_for('college.data'))
        except:
            flash(f"College {collegeCode.upper()} Already Exists! Cannot Edit Current College To Existing College.", "error")
            return redirect (url_for('college.data'))
        

@college.route('/college/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        data = (id,)
        collegeModel.delete(data)
        flash(f"College {id.upper()} Deleted Successfully!", "info")
        return redirect(url_for('college.data'))