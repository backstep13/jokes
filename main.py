from flask import Flask, render_template, jsonify
import os
import json
import random
from pathlib import Path


app_dir = Path(__file__).resolve().parent
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route("/api/")
def get_item():
	num = random.randint(0, 16)
	file = os.path.join(app_dir, 'storage.json')
	with open(file) as f:
		data = json.load(f)		
	return jsonify(data['texts'][num]['text'])
	