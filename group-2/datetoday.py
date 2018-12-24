from flask import Flask,redirect,jsonify, url_for,request,render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html');


@app.route('/getday1/',methods=['POST'])
def getday():
	dt=request.form.get('date');
	if dt:
		return redirect(url_for('computeday',dt=dt))
	else:
		return jsonify({'error':'missing data'})
		 

@app.route('/computeday/<dt>')
def computeday(dt):
	try:
		day, month, year = (int(x) for x in dt.split('-'))    
		ans = datetime.date(year, month, day)
		weekday= ans.strftime("%A")
		return redirect(url_for('displayday',name=weekday))
	except:
		return jsonify({'error':'invalid date'})



@app.route('/displayday/<name>')
def displayday(name):
	return jsonify({'name1':name})
	
if __name__=='__main__':
	app.run(debug=True)