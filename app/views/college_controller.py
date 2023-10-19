from flask import Blueprint, render_template, request, redirect, url_for
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
            return redirect (url_for('college.data', success = True))
        except: 
            return redirect (url_for('college.data', error = True))


@college.route('/college/update', methods = ['POST'])
def update():
    if request.method == "POST":

        college_code = request.form['college_code_edit']
        name_edit = request.form['name_edit']
        print(name_edit)
        list = [name_edit.title(), college_code]
        print(list)
        try:
            collegeModel.update(list)
            return redirect (url_for('college.data', success = True))
        except: 
            return redirect (url_for('college.data', error = True))
        

@college.route('/college/delete/<string:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        data = (id,)
        collegeModel.delete(data)
        return redirect(url_for('college.data', success=True))