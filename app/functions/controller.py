from flask import render_template, redirect, request, jsonify
from app.functions import forms
from . import students_bp, courses_bp, colleges_bp
import app.models as models