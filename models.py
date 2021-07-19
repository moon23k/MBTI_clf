from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	__tablename__ = 'User'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(32), unique=True, nullable=False)
	userid = db.Column(db.String(32), unique=True, nullable=False)
	password = db.Column(db.String(32), nullable=False)


	def __init__(self, email, userid, password):
		self.email = email
		self.userid = userid
		self.set_password(password)

	def set_password(self, password):
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def __repr__(self):
		return f"< User {self.userid} >"


