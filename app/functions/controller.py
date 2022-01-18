from flask import render_template, redirect, request, jsonify
from app.functions import forms
from . import students_bp, courses_bp, colleges_bp
import app.models as models
from app.functions.forms import CollegeForm
from app import mysql

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