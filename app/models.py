from app import mysql

class Student(object):

    def __init__(self, id = None, first = None, last = None, course = None,
                 year = None, gender = None, upload = None):
        self.id = id
        self.first = first
        self.last = last
        self.course = course
        self.year = year
        self.gender = gender
        self.upload = upload

    def addstudent(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO students(stud_id,firstName,lastName,course,yearLevel,gender,image) \
                VALUES('{self.id}','{self.first}','{self.last}','{self.course}','{self.year}','{self.gender}', '{self.upload}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editstudent(self):
        cursor = mysql.connection.cursor()
        print(self.id)
        if self.upload:
            sql = f"UPDATE students SET stud_id ='{self.id}',firstName ='{self.first}',lastName ='{self.last}',course ='{self.course}',yearLevel ='{self.year}'," \
                f"gender ='{self.gender}', image ='{self.upload}' WHERE stud_id = '{str(self.id)}'"
            print(sql, "With Image")
        else:
            sql = f"UPDATE students SET stud_id ='{self.id}',firstName ='{self.first}',lastName ='{self.last}',course ='{self.course}',yearLevel ='{self.year}'," \
                f"gender ='{self.gender}' WHERE stud_id = '{str(self.id)}'"
            print(sql, "Without Image")
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allstudent(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deletestudent(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from students where stud_id = '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchstudent(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from students where stud_id='{id}'"
        cursor.execute(sql)
        ids = cursor.fetchall()
        return ids

class Course(object):

    def __init__(self, course_code = None, course_name = None, course_college = None):
        self.course_code = course_code
        self.course_name = course_name
        self.course_college = course_college

    def addcourse(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO courses(courseCode,courseName,courseCollege) \
                VALUES('{self.course_code}','{self.course_name}','{self.course_college}')"
        cursor.execute(sql)
        mysql.connection.commit()

    def editcourse(self):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE courses SET courseCode ='{self.course_code}',courseName ='{self.course_name}',courseCollege ='{self.course_college}'" \
              f"WHERE courseCode = '{str(self.course_code)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allcourse(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    @classmethod
    def deletecourse(cls, course_code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from courses where courseCode = '{course_code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchcourse(cls, course_code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from courses where courseCode='{course_code}'"
        cursor.execute(sql)
        codes = cursor.fetchall()
        return codes

class College(object):

    def __init__(self, college_code = None, college_name = None):
        self.college_code = college_code
        self.college_name = college_name

    def addcollege(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO colleges(collegeCode,collegeName) \
                VALUES('{self.college_code}','{self.college_name}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editcollege(self):
        cursor = mysql.connection.cursor()
        print(self.college_code)
        sql = f"UPDATE colleges SET collegeCode ='{self.college_code}',collegeName ='{self.college_name}' WHERE collegeCode = '{str(self.college_code)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allcollege(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deletecollege(cls, college_code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from colleges where collegeCode = '{college_code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchcollege(cls, college_code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from colleges where collegeCode='{college_code}'"
        cursor.execute(sql)
        codecs = cursor.fetchall()
        return codecs