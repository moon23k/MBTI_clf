from flask import Blueprint, render_template, url_for, request
from models import User
from tweets import get_tweets
from get_mbti import clean_text, get_result


search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template('search.html')

    else:
        search_name = request.form['search_name']
        tweets = get_tweets(search_name)

        if not tweets:
            flash(f'{search_name}에 대한 검색 결과가 없습니다.')
            return render_template('search.html')
        
        words = clean_text(tweets)
        result = get_result(words)

        return render_template('search.html', search_name=search_name, result=result[0])


