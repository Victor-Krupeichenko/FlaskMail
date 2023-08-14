from flask import Flask, render_template

from recipient_list_file.routers import recipient_router
from mailing_list.routers import mailing_list
from settings_env import secrets_key_csrf

app = Flask(__name__)

app.secret_key = secrets_key_csrf
app.register_blueprint(recipient_router)
app.register_blueprint(mailing_list)


@app.route("/")
def home():
    return render_template("index.html")
