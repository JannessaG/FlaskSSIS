from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField

class StudentForm(FlaskForm):
    id = StringField ("stud_id", [validators.DataRequired(),validators.Regexp("\d\d\d\d-\d\d\d\d")])
    first = StringField ("firstName", [validators.DataRequired()])
    last = StringField ("lastName", [validators.DataRequired()])
    course = SelectField ("course", choices=[])
    year = SelectField('yearLevel', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    gender = SelectField("gender", choices=[('Male','Male'),('Female','Female')])
    upload = FileField('image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField("Submit")

    def __init__(self, id = None, first = None, last = None, course = None, year = None, gender = None, upload = None):
        super().__init__()
        if id:
            self.process()
            self.id.default = id
            self.first.default = first
            self.last.default = last
            self.course.default = course
            self.year.default = year
            self.gender.default = gender
            self.upload.default = upload
            self.process()

class CourseForm(FlaskForm):
    course_code = StringField("courseCode", [validators.DataRequired()])
    course_name = StringField("courseName", [validators.DataRequired()])
    course_college = SelectField("courseCollege", choices=[])
    submit = SubmitField("Submit")

    def __init__(self, course_code = None, course_name = None, course_college = None):
        super().__init__()
        if course_code:
            self.process()
            self.course_code.default = course_code
            self.course_name.default = course_name
            self.course_college.default = course_college
            self.process()

class CollegeForm(FlaskForm):
    college_code = StringField("collegeCode", [validators.DataRequired()])
    college_name = StringField("collegeName", [validators.DataRequired()])
    submit = SubmitField("Submit")

    def __init__(self, college_code = None, college_name = None):
        super().__init__()
        if college_code:
            self.process()
            self.college_code.default = college_code
            self.college_name.default = college_name
            self.process()