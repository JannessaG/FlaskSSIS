from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField

class CourseForm(FlaskForm):
    course_code = StringField("courseCode", [])
    course_name = StringField("courseName", [])
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
    college_code = StringField("collegeCode", [])
    college_name = StringField("collegeName", [])
    submit = SubmitField("Submit")

    def __init__(self, college_code = None, college_name = None):
        super().__init__()
        if college_code:
            self.process()
            self.college_code.default = college_code
            self.college_name.default = college_name
            self.process()