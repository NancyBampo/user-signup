from flask import Flask, request, redirect, render_template
import html

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/signup', methods=["POST"])
def display_signup():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]
    
    



app.run()