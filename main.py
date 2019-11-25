from flask import Flask, request, redirect, render_template
import html

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    
    return render_template('signup.html')


@app.route('/', methods=["POST"])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]


    user_error = ""
    pass_error = ""
    vp_error = ""
    email_error = ""

    if username == "":
        user_error = "That's not a valid username"
        username = ''
    else:
        if len(username) < 3 or len(username) > 20:
            user_error = "That's not a valid username"
            username = '' 
        else:
            if " " in username:
                user_error = "That's not a valid username"
                username = ""

    if password == "":
        pass_error = "That's not a valid password"
        password = ''
    else:
        if len(password) < 3 or len(password) > 20:
            pass_error = "That's not a valid password"
            password = ''
        else:
            if " " in password:
                pass_error = "That's not a valid password"
                password = ""

    if verify_password == "":
        vp_error = 'Passwords do not match'
        verify_password = ''
    else:
        if password != verify_password:
            vp_error = "Passwords do not match"
            verify_password = ''  
    

    if len(email) > 0:
        if "@" not in email or "." not in email or " " in email:
            email_error = "That's not a valid email"
            email = ''
        else:
            if len(email) < 3 or len(email) > 20:
                email_error = "That's not a valid email"
                email = ''
        
        
    if not user_error and not pass_error and not vp_error and not email_error:
        username = str(username)
        return render_template("welcome_form.html", username=username)
    else:
        return render_template('signup.html', user_error=user_error, pass_error=pass_error, 
        vp_error=vp_error, email_error=email_error, username=username, password=password,
        verify_password=verify_password, email=email)

    

    

@app.route('/welcome', methods=["POST"])
def welcome():
    username = request.form["username"]
    return render_template("welcome_form.html", username=username)


app.run()