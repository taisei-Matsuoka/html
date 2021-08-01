from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    age = request.form['age']
    db = request.form['dateofbirth']
    return render_template('pass.html', n=name, age=age,db=db)