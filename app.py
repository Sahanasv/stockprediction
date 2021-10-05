
from flask import Flask, render_template,request,session

from sklearn.metrics import accuracy_score

import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1',methods=['GET','POST'])
def pred():
    a=[]
    if request.method=="POST":
        open = request.form['op']
        low = request.form['low']
        high = request.form['high']
        vol = request.form['vol']
        a.extend([open,low,high,vol])
        model=joblib.load('bank1.pkl')
        y_pred=model.predict([a])
        return render_template('prediction.html',msg="success",op=y_pred)
    return render_template('prediction.html')


if __name__ == '__main__':
    app.secret_key="sahana"
    app.run(debug=True)
