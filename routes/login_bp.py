from flask import Blueprint, render_template, redirect, url_for, request, session
from authentications.login_auth import login

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["POST", "GET"])
def login_page():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return None
        logging_in = login(username, password)    
        if not logging_in:
            error = "Wrong Password or Username"
            return render_template("login.html", error=error) 
        return "yey"    
    return render_template("login.html", error=error)    