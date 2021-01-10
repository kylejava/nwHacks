from flask import Flask, render_template, flash, request
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def index():
    return render_template('index.html')

@app.route('/getstarted' , methods = ['GET' , 'POST'])
def getstarted():
    return render_template('getstarted.html')

@app.route('/signin' , methods = ['GET' , 'POST'])
def signin():
    return render_template('signin.html')

@app.route('/signup' , methods = ['GET' , 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/templates' , methods = ['GET' , 'POST'])
def teplates():
    return render_template('templates.html')

@app.route('/userinput' , methods = ['GET' , 'POST'])
def userinput():
    return render_template('userinput.html')

@app.route('/template1' , methods = ['GET' , 'POST'])
def template1():
    return render_template('template1.html')

if __name__ == "__main__":
    app.run(debug=True)
