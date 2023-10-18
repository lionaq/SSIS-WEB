from flask import Blueprint, render_template
from app.Models import studentModel

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    result = studentModel.all()
    print(result)
    return render_template('student.html', data = result)