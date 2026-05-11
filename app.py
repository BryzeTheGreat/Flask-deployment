from flask import Flask
from routes.login_bp import login_bp
from routes.register_bp import register_bp


app = Flask(__name__)
app.config["SECRET_KEY"] = "d17d1b5fb3f1f6c57758b3bb10376a6d1b59e9f3cd1c040f0931327f7b18"

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

if __name__ == "__main__":
    app.run()
