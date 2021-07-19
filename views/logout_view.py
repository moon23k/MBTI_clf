from flask import Blueprint, render_template, request, session

logout_bp = Blueprint('logout', __name__, url_prefix='/logout')


@login_bp.route('/logout')
def login():
    session.pop('userid', None)
    return redirect('/')