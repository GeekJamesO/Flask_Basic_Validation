from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "MaryHadaLittleLamb"

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'] )
def process():
    if (len(request.form['name']) < 1 ):
        flash("Name cannot be empty")
    else:
        flash("Success!  Your name is {}".format(request.form['name']))
    return redirect('/')

app.run(debug=True)
