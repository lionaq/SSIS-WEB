from flask import Blueprint, render_template
from app.Models import collegeModel

college = Blueprint('college', __name__)

@college.route('/college')
def data():
    result = collegeModel.all()
    print(result)
    return render_template('college.html', data = result)