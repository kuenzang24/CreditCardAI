import pickle
import pandas as pd
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model.pkl',"rb"))

cols = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11','A12', 'A13', 'A14', 'A15']
#x_sample = pd.DataFrame([['b', 23.92, 0.665, 'u', 'g', 'c', 'v', 0.165, 'f', 'f', 0, 'f','g', 100.0, 0]],columns=cols)
#result = model.predict(x_sample)
#print("The output for given sample is",result[0])

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def prediction():
    if request.method == "POST":
        A1 = request.form['A1']
        A2 = float(request.form['A2'])
        A3 = float(request.form['A3'])
        A4 = request.form['A4']
        A5 = request.form['A5']
        A6 = request.form['A6']
        A7 = request.form['A7']
        A8 = float(request.form['A8'])
        A9 = request.form['A9']
        A10 = request.form['A10']
        A11 = float(request.form['A11'])
        A12 = request.form['A12']
        A13 = request.form['A13']
        A14 = float(request.form['A14'])
        A15 = float(request.form['A15'])

        x_sample = [[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15]]
        X = pd.DataFrame(x_sample,columns=cols)
        result = model.predict(X)
        return render_template("output.html",value=result)


if __name__=="__main__":
    app.run()