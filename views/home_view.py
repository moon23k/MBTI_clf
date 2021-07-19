from flask import Blueprint, render_template, session


#BluePrint 객체선언
home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/', methods=['GET'])
def home():
	userid = session.get('userid')

	if userid:
		return render_template('home.html', userid=userid)
	return render_template('home.html')	
