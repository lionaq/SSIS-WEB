from app import mysql

class students(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_table")
        students = cursor.fetchall()
        cursor.close()
        return students

        
studentModel = students()