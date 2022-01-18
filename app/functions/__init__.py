from flask import Blueprint

students_bp = Blueprint('students',__name__)
courses_bp  = Blueprint('courses',__name__)
colleges_bp = Blueprint('colleges', __name__)

from . import controller