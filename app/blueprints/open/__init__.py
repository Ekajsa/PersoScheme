from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.controllers.user_controller import create_user, verify_user, get_user_by_email, signin_user

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('index.html')


@bp_open.get("/signup")
def signup_get():
    return render_template("signup.html")


@bp_open.post("/signup")
def signup_post():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]

    if get_user_by_email(email) is not None:
        flash("Error. An account with this email already exists.")
        return redirect(url_for("bp_open.signup_get"))

    create_user(first_name, last_name, email, password)
    return redirect(url_for("bp_open.signin_get"))


@bp_open.get("/signin")
def signin_get():
    return render_template("signin.html")


@bp_open.post("/signin")
def signin_post():
    email = request.form.get("email")
    password = request.form.get("password")
    if not verify_user(email, password):
        flash("Error signing in. Check your email and password!")
        return redirect(url_for("bp_open.signin_get"))

    signin_user(email)

    return redirect(url_for("bp_open.index"))



# @bp_open.get('/about')
# def about():
#     return render_template('about.html')
