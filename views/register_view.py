from flask import Blueprint, render_template, url_for, redirect, flash, request
from models import User
from app import db


#BluePrint 객체선언
register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    else:
        userid = request.form.get('userid')
        email = request.form.get('email')
        password = request.form.get('password')
        password_2 = request.form.get('re_password')


        existing_id = User.query.filter_by(userid=userid).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_id:
            flash("이미 사용중인 아이디 입니다.")
            return render_template('register.html')

        if existing_email:
            flash("이미 사용중인 이메일 입니다.")
            return render_template('register.html')

        if not(userid and email and password and password_2):
            flash("입력되지 않은 정보가 있습니다")
            return render_template('register.html')

        elif password != password_2:
            flash("비밀번호가 일치하지 않습니다")
            return render_template('register.html')

        else:
            user = User(email=email, userid=userid, password=password)
            db.session.add(user)
            db.session.commit()
            flash("회원가입 완료! 로그인 해주세요.")
        
        return render_template('register.html')

