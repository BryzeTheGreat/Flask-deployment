from connections.connect import Session
from connections.models import Accounts
from werkzeug.security import check_password_hash

session = Session()

def login(username, password):
    user = session.query(Accounts).filter_by(username=username).first()
    if user:
        password_verify = check_password_hash(user.password, password)
        return user
    return None