from flask import Flask, request,render_template
import pandas as pd

import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)


app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		return render_template('home.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
	
@app.route('/pro')
def pro():
   return render_template("pro.html")
	
@app.route('/home')
def home():
   return render_template("home.html")


@app.route("/red")

def red():
    
 pn='A2CL818RN52NWN'
 pred = pd.read_csv("out.csv")
 nac=pred[pred["uid"] == pn][["iid", "r_ui","est"]].sort_values(by = "est",ascending = False)
 
 nac=nac['iid'].values.tolist()
 return render_template("pro.html", list=nac)
@app.route("/MT1")
def MT1():
    
 pn='AKT8TGIT6VVZ5'
 pred = pd.read_csv("out.csv")
 nac=pred[pred["uid"] == pn][["iid", "r_ui","est"]].sort_values(by = "est",ascending = False)
 
 nac=nac['iid'].values.tolist()
 return render_template("mt.html", list=nac)

@app.route("/r15")
def r15():
    
 pn='A2XRMQA6PJ5ZJ8'
 pred = pd.read_csv("out.csv")
 nac=pred[pred["uid"] == pn][["iid", "r_ui","est"]].sort_values(by = "est",ascending = False)
 
 nac=nac['iid'].values.tolist()
 return render_template("r1.html", list=nac)
@app.route("/ac")
def ac():
    
 pn='ALUNVOQRXOZIA'
 pred = pd.read_csv("out.csv")
 nac=pred[pred["uid"] == pn][["iid", "r_ui","est"]].sort_values(by = "est",ascending = False)
 
 nac=nac['iid'].values.tolist()
 return render_template("ac.html", list=nac)
@app.route("/handle", methods=["POST"])

def handle():
    
 pn=request.form.get("pname")
 pred = pd.read_csv("out.csv")
 nac=pred[pred["uid"] == pn][["iid", "r_ui","est"]].sort_values(by = "est",ascending = False)
 
 nac=nac['iid'].values.tolist()
 return render_template("nav.html", list=nac)
 
 
if __name__ == '__main__':
   app.debug = True
   app.run()