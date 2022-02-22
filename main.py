from flask import Flask, render_template, jsonify
from pathlib import Path
import os
import json
import random


app_dir = Path(__file__).resolve().parent  # project path
app = Flask(__name__)

@app.route("/")
def index():
	"""Function return HTML of main page"""
	return render_template('index.html')
	
@app.route("/api/")
def get_item():
	"""Function return JSON answer from storage to client """
	num = random.randint(0, 16)
	file = os.path.join(app_dir, 'storage.json')
	with open(file, 'r', encoding='utf-8') as f:
		data = json.load(f)
	return jsonify(data['texts'][num]['text'])
