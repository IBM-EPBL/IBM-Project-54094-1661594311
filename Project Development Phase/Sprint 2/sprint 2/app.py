import flask
from flask import request, render_template
from flask_cors import CORS
import joblib
 
app = flask.Flask(__name__, static_url_path='')
CORS(app)
 
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('another.html')
 
@app.route('/predict', methods=['POST'])
def predictSpecies():
    cly = float(request.form['cly'])
    dis = float(request.form['dis'])
    hp = float(request.form['hp'])
    w= float(request.form['w'])
    a = float(request.form['a'])
    my = float(request.form['my'])
    ori = float(request.form['ori'])
    X = [[cly,dis,hp,w,a,my,ori]]
    model = joblib.load('regression.pkl')
    species = model.predict(X)[0]
    return render_template('predict.html',predict=species)
 
if __name__ == '__main__':
    app.run()
 


