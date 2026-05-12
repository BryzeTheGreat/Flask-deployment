from connections.models import Accounts, Session
import secrets
from werkzeug.security import generate_password_hash
import uuid

session = Session()

def register_account(username, password):
    hashed_password = generate_password_hash(password)
    uid = str(uuid.uuid4())
    user = Accounts(uid=uid, username=username, password=hashed_password)    
    session.add(user)
    session.commit() 
    return uid
    
def user_verification(username):
    result = session.query(Accounts).filter_by(username=username).first()
    return result 