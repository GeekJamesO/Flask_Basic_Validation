from flask import Flask, render_template, request, redirect, flash
import re #regular Expressions

app = Flask(__name__)
app.secret_key = "MaryHadaLittleLamb"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'] )
def process():
    if (len(request.form['name']) < 1 ):
        flash("Name cannot be empty")
    else:
        flash("Success!  Your name is {}".format(request.form['name']))

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("'{}' is an invalid Email Address!".format(request.form['email']))
    else:
        flash("Success! - email is valid")

    return redirect('/')

app.run(debug=True)
