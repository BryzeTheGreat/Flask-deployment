from flask import Blueprint, render_template, request, session
from connections.models import Accounts
from werkzeug.security import generate_password_hash
from authentications.register_auth import register_account, user_verification
import uuid


register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["POST", "GET"])
def register_page():
    error = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            error = "Invalid"
        else:    
            user_valid = user_verification(username)
        if user_valid:
            error="Username Already Taken"   
        else:    
            account = register_account(username, password) 
            user = user_verification(username)
            session['user'] = user.uid
            return "SUCCESS"  
    return render_template('register.html', error=error)