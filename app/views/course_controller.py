from flask import Blueprint, render_template
from app.Models import courseModel

course = Blueprint('course', __name__)

@course.route('/course')
def data():
    result = courseModel.all()
    print(result)
    return render_template('course.html', data = result)