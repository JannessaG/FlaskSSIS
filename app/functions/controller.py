from flask import render_template, redirect, request, jsonify
from app.functions import forms
from . import students_bp, courses_bp, colleges_bp
import app.models as models
from app.functions.forms import CourseForm,CollegeForm
from app import mysql

def fetch_from_table(table_name, column):
    cursor = mysql.connection.cursor()
    sql = f"SELECT {column} from {table_name}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

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