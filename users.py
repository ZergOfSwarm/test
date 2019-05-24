import flask import Flask
frome users import users

me flask import Blueprint

users = Blueprint('users', ''__name__ )

app.register_blueprint(users)
@users.route("/")
def index():
    return render_template("template.html",title='Welcome to our page!',greeting='Welcome Hooman', masage'We are glad you came!')

@users.route("/users/home")
def userhome():
    return render_template("template.html",title='Users!',greeting='Hello user!', masage'How are you?')
