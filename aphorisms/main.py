from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aphorisms.db'
db = SQLAlchemy(app)
api = Api(app)


class Aphorism(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text, nullable=False)


@app.route("/")
def index():
	"""Function return HTML of main page"""
	return render_template('index.html')


class Item(Resource):
	def get(self):
		"""Function return JSON answer from db to client """
		num = random.randint(0, 16)
		data = Aphorism.query.get(num)
		return data.text


api.add_resource(Item, '/api')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
