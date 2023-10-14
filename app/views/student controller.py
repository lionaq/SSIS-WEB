from flask import Blueprint

student = Blueprint('student', __name__)

@student.route('/student')
    def data():
        return render_template('student.html')