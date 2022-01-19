from flask import render_template, redirect, request, jsonify
from app.functions import forms
from . import students_bp, courses_bp, colleges_bp
import app.models as models
from app.functions.forms import StudentForm,CourseForm,CollegeForm
from app import mysql
import cloudinary
import cloudinary.api
import cloudinary.uploader

def fetch_from_table(table_name, column):
    cursor = mysql.connection.cursor()
    sql = f"SELECT {column} from {table_name}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@students_bp.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        students = models.Student.allstudent()
        course = models.Course.allcourse()
        college = models.College.allcollege()
        return render_template('student.html', data=students,data1=course,data2=college, geturl='.main')

@students_bp.route('/viewstudents', methods=['POST', 'GET'])
def mainstudent():
    if request.method == 'GET':
        students = models.Student.allstudent()
        course = models.Course.allcourse()
        college = models.College.allcollege()
        return render_template('student.html', data=students,data1=course,data2=college, geturl='.mainstudent')

@students_bp.route('/viewstudents/add', methods=['POST', 'GET'])
def addstudent():
    form = StudentForm()
    for row in fetch_from_table('courses', 'courseCode'):
        course = str(row[0])
        form.course.choices += [(course, course)]
    if request.method == 'POST' and form.validate():
        if bool(form.upload.data):
            req = cloudinary.uploader.upload(form.upload.data.stream, public_id = form.id.data)
            req = req["secure_url"]
            #print(req)
        else:
            req = None

        student = models.Student(id=form.id.data, first=form.first.data, last=form.last.data, course=form.course.data,
                           year=form.year.data, gender=form.gender.data, upload=req)
        student.addstudent()
        return redirect('/viewstudents')
    else:
        return render_template('addStudent.html', form=form, geturl=".addstudent")

@students_bp.route("/viewstudents/edit", methods=['POST', 'GET'])
def editstudent():
    if request.method == 'GET':
        id = request.args.get("id")
        students = models.Student(id=id)
        studentinfo = students.searchstudent(id)
        form = StudentForm(studentinfo[0][0], studentinfo[0][1], studentinfo[0][2], studentinfo[0][3], studentinfo[0][4], studentinfo[0][5])
        for row in fetch_from_table('courses', 'courseCode'):
            course = str(row[0])
            form.course.choices += [(course, course)]
    else:
        form = StudentForm()
        for row in fetch_from_table('courses', 'courseCode'):
            course = str(row[0])
            form.course.choices += [(course, course)]

    if request.method == 'POST' and form.validate():

        if bool(form.upload.data):
            req = cloudinary.uploader.upload(form.upload.data.stream, public_id=form.id.data)
            req = req["secure_url"]
            #print(req)
        else:

            req = None
        student = models.Student(id=form.id.data, first=form.first.data, last=form.last.data, course=form.course.data,
                           year=form.year.data, gender=form.gender.data, upload=req)
        student.editstudent()
        return redirect('/viewstudents')
    else:
        return render_template('editStudent.html', form=form,geturl='.editstudent')

@students_bp.route("/viewstudents/delete", methods=["POST"])
def deletestudent():
    id = request.form['id']
    if models.Student.deletestudent(id):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")

#---------------------------------------------------------------------
@courses_bp.route('/viewcourses', methods=['POST', 'GET'])
def maincourse():
    if request.method == 'GET':
        course = models.Course.allcourse()
        college = models.College.allcollege()
        return render_template('course.html', data=course, data1=college)

@courses_bp.route('/viewcourses/add', methods=['POST', 'GET'])
def addcourse():
    form = CourseForm()
    for row in fetch_from_table('colleges', 'collegeCode'):
        college = str(row[0])
        form.course_college.choices += [(college, college)]
    if request.method == 'POST' and form.validate():
        course = models.Course(course_code=form.course_code.data, course_name=form.course_name.data, course_college=form.course_college.data)
        course.addcourse()
        return redirect('/viewcourses')
    else:
        return render_template('addCourse.html', form=form, geturl=".addcourse")

@courses_bp.route("/viewcourses/edit", methods=['POST', 'GET'])
def editcourse():
    if request.method == 'GET':
        course_code = request.args.get("id")
        course = models.Course(course_code=id)
        courseinfo = course.searchcourse(course_code)
        form = CourseForm(courseinfo[0][0], courseinfo[0][1], courseinfo[0][2])
        for row in fetch_from_table('colleges', 'collegeCode'):
            college = str(row[0])
            form.course_college.choices += [(college, college)]
    else:
        form = CourseForm()
        for row in fetch_from_table('colleges', 'collegeCode'):
            college = str(row[0])
            form.course_college.choices += [(college, college)]

    if request.method == 'POST' and form.validate():
        course = models.Course(course_code=form.course_code.data, course_name=form.course_name.data, course_college=form.course_college.data)
        course.editcourse()
        return redirect('/viewcourses')
    else:
        return render_template('editCourse.html', form=form, geturl='.editcourse')

@courses_bp.route("/viewscoursess/delete", methods=["POST"])
def deletecourse():
    course_code= request.form['id']
    if models.Course.deletecourse(course_code):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")


#-----------------------------------------------------------------------------------
@colleges_bp.route('/viewcolleges', methods=['POST', 'GET'])
def maincollege():
    if request.method == 'GET':
        college = models.College.allcollege()
        print(college)
        return render_template('college.html', data=college)

@colleges_bp.route('/viewcolleges/add', methods=['POST', 'GET'])
def addcollege():
    form = CollegeForm()

    if request.method == 'POST' and form.validate():
        print("in")
        college = models.College(college_code=form.college_code.data, college_name=form.college_name.data)
        print(college)
        college.addcollege()
        return redirect('/viewcolleges')
    else:
        return render_template('addCollege.html', form=form, geturl=".addcollege")

@colleges_bp.route("/viewcolleges/edit", methods=['POST', 'GET'])
def editcollege():
    if request.method == 'GET':
        college_code = request.args.get("id")
        college = models.College(college_code=id)
        collegeinfo = college.searchcollege(college_code)
        form = CollegeForm(collegeinfo[0][0], collegeinfo[0][1])
        print(form, "collegeeditform")

    else:
        form = CollegeForm()

    if request.method == 'POST' and form.validate():
        college = models.College(college_code=form.college_code.data, college_name=form.college_name.data)
        print(college, "College Edit")
        college.editcollege()
        return redirect('/viewcolleges')
    else:
        return render_template('editCollege.html', form=form, geturl='.editcollege')

@colleges_bp.route("/viewcolleges/delete", methods=["POST"])
def deletecollege():
    college_code = request.form['id']
    print(college_code, "Delete ID")
    if models.College.deletecollege(college_code):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")