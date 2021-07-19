from flask import Blueprint, render_template, request, session, flash
from models import User
from werkzeug.security import generate_password_hash, check_password_hash


#BluePrint 객체선언
login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        userid = request.form['userid']
        password = request.form['password']
        
        data = User.query.filter_by(userid=userid).first()
        
        if data is None:
            flash('존재하지 않는 아이디 입니다.')
            return render_template('login.html')
        
        elif check_password_hash(generate_password_hash(password), password) + check_password_hash(data.password, password) != 2:
            flash('비밀번호를 확인해주세요')
            return render_template('login.html')

        session['userid'] = userid
        return render_template('home.html')




logout_bp = Blueprint('logout', __name__, url_prefix='/logout')

@login_bp.route('/')
def logout():
    session.pop('userid', None)
    return render_template('home.html')