import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

db = SQLAlchemy()


def create_app(config=None):
	app = Flask(__name__)
	
	#configurations
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	app.config['SECRET_KEY'] = 'super secret key'
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	
	if config is not None:
		app.config.update(config)

	#initialize db	
	db.init_app(app)
	db.app = app

	#import bp
	from views.home_view import home_bp
	from views.search_view import search_bp
	from views.login_view import login_bp, logout_bp
	from views.register_view import register_bp

	#register bp
	app.register_blueprint(home_bp)
	app.register_blueprint(search_bp)
	app.register_blueprint(login_bp)
	app.register_blueprint(logout_bp)
	app.register_blueprint(register_bp)

	return app


if __name__ == '__main__':
	app = create_app()
	db.create_all()
	app.run(debug=True)
