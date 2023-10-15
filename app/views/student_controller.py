from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/student')
def data():
    return render_template('student.html')