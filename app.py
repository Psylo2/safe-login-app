from dotenv import load_dotenv

load_dotenv(".env", verbose=True)

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

from app_configuration import AppConfiguration

from logic import UserLogic, AdminLogic

from views.users import user_blueprint
from views.admins import admin_blueprint

app = Flask(__name__)
csrf = CSRFProtect(app)

AppConfiguration(app=app)

@app.get('/')
def home():
    return render_template('home.html')


user_blueprint.handler = UserLogic()
admin_blueprint.handler = AdminLogic()

app.register_blueprint(user_blueprint,
                       url_prefix="/users")

app.register_blueprint(admin_blueprint,
                       url_prefix="/admin")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
