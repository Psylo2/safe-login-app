from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)

from views.users import user_blueprint
from views.admins import admin_blueprint

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.update(SECRET_KEY=os.environ.get('APP_SECRET_KEY'),
                  WTF_CSRF_SECRET_KEY=os.environ.get('SECRET_KEY_CSRF'),
                  ADMIN=os.environ.get('ADMIN_NAME'))

@app.get('/')
def home():
    return render_template('home.html')


app.register_blueprint(user_blueprint,
                       url_prefix="/users")

app.register_blueprint(admin_blueprint,
                       url_prefix="/admin")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
