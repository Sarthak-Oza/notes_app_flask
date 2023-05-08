from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_remembered, login_required

from datab import db
from models import *


from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()    

        if user:
            print("record exist")

            if check_password_hash(User.query.filter_by(email=email).first().password, password):
                print("password matches")
                # login_user(user, remember=True)
                login_user(user)
                return redirect(url_for("Views.home", user = user))
            else:
                flash("Please enter correct password!", category="error")

        else:
            flash("Account does not exist, please signup!", category="error")
            print("non existing user")
            return redirect(url_for("auth.signup"))
    return render_template("login.html")

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        

        if not name or not password:
            flash("Please complete the form to sign up!", category="error")
        else:
            print(request.form)
            user = User(name = name, email = email, password = generate_password_hash(password, method="sha256"))
            db.session.add(user)
            db.session.commit()
            
           
            
            
            flash("Account created successfully!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("Views.home"))
        


    return render_template("signup.html")

@auth.route("/logout")
# @login_required
def logout():
    print(current_user)
    if not current_user:
        print("current user?")
        flash("Please login", category="error")
        redirect(url_for("Views.home"))
    else:
        logout_user()
        return redirect(url_for("auth.login"))

    

@auth.route("/notesadd", methods = ["POST"])
@login_required
def notesadd():
    print(current_user.id)
    note = Note(data = request.form.get("notestext"), user_id = current_user.id)
    db.session.add(note)
    db.session.commit()

    return redirect(url_for("Views.home"))

@auth.route("/deletenote/<int:id>", methods = ["POST"])
@login_required
def notedelete(id):
    print(id)
    note = Note.query.filter_by(id=id).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("Views.home"))
    

@auth.route("/updatenote/<int:id>")
@login_required
def updatenote(id):
    print("update note id", id)
    return render_template("update.html", user = current_user, note_id = id)

@auth.route("/updatedb/<int:id>", methods = ["POST"])
@login_required
def updatedb(id):
    print("update db id -> ", id)
    print("updated text ->", request.form.get("updatedtext"))
    note = Note.query.filter_by(id=id).first()
    note.data = request.form.get("updatedtext")
    db.session.commit()

    return redirect(url_for("Views.home"))
