from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import random
import time

app = Flask(__name__) 

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error(error)
	return render_template('page_not_found.html'), 404

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/upload')
def upload_page():
	return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save('./uploads/' + secure_filename(f.filename))
		tmp = os.path.join("uploads", f.filename)
		result = os.popen("./darknet detector test data/food.data cfg/yolov3-tiny_obj.cfg final.weights %s" %(tmp))

		lines = result.read().split("\n")
		print(lines[1:])

		#CALORIE calculator 
		c = calorie(lines[1:])
		print("calorie : %d" %(c))
		time.sleep(2)

		idx =random.randrange(1,50000)
		tmp2 = "%d.jpg" %idx
		# Move generated image files into static folder
		os.popen("cp %s static/images/" %(tmp))
		rt = os.popen("cp predictions.jpg static/images/%s" %(tmp2))

		return render_template('check.html', bf_image=f.filename, a_image=tmp2, txt="%d KCAL" %(c)) # calorie 
	else:
		return render_template('page_not_found.html')

def calorie(text):
	food_dict = {"samgupsal": 517.9, "bulgogi": 489.0, "ojingeo_bokkeum":176.6, "dakbokkeumtang":200.9, "galchijorim":134,"jeyuk_bokkeum":192.7,\
	 "bibimbap":535.5, "galbijjim":162.9, "soondubu_jjigae":253 ,"kimchi":29,"samgyetang":918,"daegaejjim":219,"soondae":235, "nangmyeon":380,\
	 "gimbob":450, "bossam":581, "doenjang_chigae":36.22, "ganjang_gejang":379, "jjajangmyeon":674, "pajeon":240, "bob":313	}

	overall = 0

	for line in text:
		if (line == ''):
			break
		line = line.split(":")
		overall += food_dict[line[0]]

	return overall

if __name__ == '__main__':
	app.run(host='eelab9.kaist.ac.kr', port=8080, debug = True)
