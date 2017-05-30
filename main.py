from flask import Flask
from config import DevConfig
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)




class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return  "<User '{}'>".format(self.username)



@app.route('/')
def home():
    return '<h1>hello world!</h1>'


if __name__ == '__main__':
    app.run()



