from flask import render_template, redirect, request, flash
from users_cr_app import app
from users_cr_app.models.users_model import User

@app.route('/', methods=["GET"])
def home():
    return redirect('/users')

@app.route('/users', methods=["GET"])
def usersListDisplay():
    usersList = User.getUsers()
    return render_template("read.html", users=usersList)

@app.route('/user/new', methods=["GET"])
def newUserForm():
    return render_template("create.html")

@app.route('/user/add', methods=["POST"])
def addUserNew():
    newUser = {
        "first_name" : request.form["firstname"],
        "last_name" : request.form["lastname"],
        "email" : request.form["email"]
    }
    result = User.addUser(newUser)
    print("Este es el resultado del INSERT:", result)
    print("Su tipo es:", type(result))
    if type(result) is int:
        return redirect('/users')
    else:
        flash("There was a problem registering the new user, please try again", "addusernew")
        return redirect('/user/new')