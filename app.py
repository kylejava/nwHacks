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
    name = ""
    email = ""
    phonenumber = ""
    address = ""
    position = ""
    website = ""
    templateSelection = ""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        address = request.form['address']
        position = request.form['position']
        website = request.form['website']
        templateSelection = request.form.get('template-selection')
        if(templateSelection == 'template-one'):
            return render_template('template1.html', name= name , email = email, phonenumber= phonenumber,address = address, position= position, website = website)
        elif(templateSelection == 'template-two'):
            return render_template('template2.html', name= name , email = email, phonenumber= phonenumber,address = address, position= position, website = website)
        elif(templateSelection == 'template-three'):
            return render_template('template3.html', name= name , email = email, phonenumber= phonenumber,address = address, position= position, website = website)
            
    return render_template('userinput.html')

if __name__ == "__main__":
    app.run(debug=True)
