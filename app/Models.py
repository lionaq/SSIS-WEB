from app import mysql

class students(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT student_table.student_id, student_table.first_name, student_table.last_name, student_table.course_code, student_table.year_level, student_table.gender, college_table.college_code FROM student_table INNER JOIN course_table on student_table.course_code = course_table.course_code JOIN college_table on course_table.college_code = college_table.college_code ORDER BY student_table.student_id")
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def insert(self, values):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "INSERT INTO student_table(student_id, first_name, last_name, course_code, year_level, gender) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()
        return
    
    def update(self, value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "UPDATE student_table SET student_id = %s, first_name = %s, last_name = %s, course_code = %s, year_level = %s, gender = %s WHERE student_id = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return
    
    def delete(self,value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "DELETE FROM student_table WHERE student_id = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return

class courses(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course_table")
        courses = cursor.fetchall()
        cursor.close()
        return courses
    
    def insert(self, values):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "INSERT INTO course_table(course_code, course, college_code) VALUES (%s, %s, %s)"
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()
        return
    
    def update(self, value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "UPDATE course_table SET course_code = %s, course = %s, college_code = %s WHERE course_code = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return

    def delete(self,value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "DELETE FROM course_table WHERE course_code = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return

    

class colleges(object):

    def all(self):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM college_table")
        colleges = cursor.fetchall()
        cursor.close()
        return colleges
    
    def insert(self, values):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "INSERT INTO college_table(college_code, name) VALUES (%s, %s)"
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()
        return
    
    def update(self, value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "UPDATE college_table SET college_code = %s, name = %s WHERE college_code = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return

    def delete(self,value):
        cursor = mysql.connection.cursor(dictionary=True)
        sql = "DELETE FROM college_table WHERE college_code = %s"
        cursor.execute(sql, value)
        mysql.connection.commit()
        cursor.close()
        return


        
studentModel = students()
courseModel = courses()
collegeModel = colleges()