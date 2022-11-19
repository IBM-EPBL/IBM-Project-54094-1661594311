from flask import request
from flask import Flask, render_template
from flask_cors import CORS
import joblib

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("a.html")

@app.route('/another')
def another():
    return render_template('another.html')    

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/contact')
def contact():
    return render_template('contact.html')    

@app.route('/Register',methods=["POST","GET"])

def Register():
    if request.method=="POST":
        cylinders=request.form.get('12')
        Displacement=request.form.get('34')
        Power=request.form.get('56')
        Weight=request.form.get('3')
        model=request.form.get('4')
        origin=request.form.get('5')
        war=request.form.get('6')
        X=[[cylinders,Displacement,Power,Weight,model,origin,war]]
        model=joblib.load("Regression.pkl")
        car=model.predict(X)[0]


        if(car >46 ):
            return render_template("result.html",Efficiency = "Very High performance with mileage"+ str(car)+"  You can plan for a tour")
        elif(car >29 and car<=46):
            return render_template("result.html",Efficiency = "High performance with mileage    "+ str(car)+"   Go for a healthy ride")
        elif(car >17.5 and car<=29):
            return render_template("result.html",Efficiency = "Medium performance with mileage  " + str(car)+"  Go for a ride nearby")
        elif(car >9 and car<=17.5):
            return render_template("result.html",Efficiency = "Low performance with mileage     "+ str(car)+"   Don't go to a long distance")
        else:
            return render_template("result.html",Efficiency = "Worst performance with mileage   "+ str(car)+"   carry extra fuel")
        

       



if __name__=='__main__':
    app.run(debug=True) 