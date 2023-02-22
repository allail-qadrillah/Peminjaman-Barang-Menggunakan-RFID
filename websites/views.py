from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')
