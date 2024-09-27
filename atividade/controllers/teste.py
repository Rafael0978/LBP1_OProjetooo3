from flask import Blueprint, render_template
from models.models import Usuario

hello_controller = Blueprint('hello', __name__)

@hello_controller.route('/')
def index():
    return render_template('index.html')


