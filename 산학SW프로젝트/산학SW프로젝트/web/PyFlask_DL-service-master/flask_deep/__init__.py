import os, sys
real_path = os.path.dirname(os.path.realpath(__file__))
sub_path = os.path.split(real_path)[0]
os.chdir(sub_path)

from flask import Flask, escape, request,  Response, g, make_response
from flask.templating import render_template
from werkzeug.utils import secure_filename
from . import prediction

app = Flask(__name__)
app.debug = True

url = ""

def root_path():
	'''root 경로 유지'''
	real_path = os.path.dirname(os.path.realpath(__file__))
	sub_path = "\\".join(real_path.split("\\")[:-1])
	return os.chdir(sub_path)

''' Main page '''
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if request.method == 'POST':
		user_img = request.files['user_img']
		user_img.save('./flask_deep/static/images/uploaded/' + str(user_img.filename))
		user_img_path = '../static/images/uploaded/' + str(user_img.filename)
		
		pred_result = prediction.main(user_img.filename)
		result = prediction.pred_to_kor(pred_result)
		sample_img_path = '../static/images/sample/' + result + '.jpg'
		return render_template('result.html', user_img=user_img_path, sample_img=sample_img_path, result = result)
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run()