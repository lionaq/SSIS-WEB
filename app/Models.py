from app import mysql

class students(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_table")
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def insert(self, values):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "INSERT INTO student_table(student_id, first_name, last_name, course_code, year_level, gender) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()
    
    def update(self, value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "UPDATE student_table SET first_name = %s, last_name = %s, course_code = %s, year_level = %s, gender = %s WHERE student_id = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
    
    def delete(self,value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "DELETE FROM course_table WHERE courseCode = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()

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