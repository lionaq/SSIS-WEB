from app import mysql

class students(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_table")
        students = cursor.fetchall()
        cursor.close()
        return students

class courses(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course_table")
        courses = cursor.fetchall()
        cursor.close()
        return courses

class colleges(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM college_table")
        colleges = cursor.fetchall()
        cursor.close()
        return colleges


        
studentModel = students()
courseModel = courses()
collegeModel = colleges()