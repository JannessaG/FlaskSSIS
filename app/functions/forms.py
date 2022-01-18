from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField

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