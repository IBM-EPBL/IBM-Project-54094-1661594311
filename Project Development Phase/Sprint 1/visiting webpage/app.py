import flask
from flask import request, render_template
from flask_cors import CORS
import joblib
 
app = flask.Flask(__name__, static_url_path='')
CORS(app)
 
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index1.html')
 
@app.route('/predict', methods=['POST'])
def predict():
    cyl=float(request.form['cyl'])
    dis=float(request.form['dis'])
    hp=float(request.form['hp'])
    w=float(request.form['w'])
    a=float(request.form['a'])
    my=float(request.form['my'])
    ori=float(request.form['ori'])
    X = [[cyl, dis, hp, w, a, my, ori]]
    model = joblib.load('regression.pkl')
    car = model.predict(X)[0]
    if(car >46 ):
     return render_template("predict.html",Efficiency = "Very High performance with mileage"+ str(car)+"You can plan for a tour")
    elif(car >29 and car<=46):
     return render_template("predict.html",Efficiency = "High performance with mileage"+ str(car)+"Go for a healthy ride")
    elif(car >17.5 and car<=29):
     return render_template("predict.html",Efficiency = 'Medium performance with mileage"'+ str(car)+"Go for a ride nearby")
    elif(car >9 and car<=17.5):
     return render_template("predict.html",Efficiency = "low performance with mileage"+ str(car)+"Don't go to a long distance")
    else:
     return render_template("predict.html",Efficiency = "worst performance with mileage"+ str(car)+"carry extra fuel")
    
 
if __name__ == '__main__':
    app.run()
 

