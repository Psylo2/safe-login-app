from flask import flash, session

from db.db import _decrypt_
from usecases import UserUseCase

from models.user import User
from models.password import Password


class UserLogic(UserUseCase):
    def __init__(self):
        pass

    def login(self, name_email: str, password: str):
        try:
            users = User.find_all_from_db()
            for user in users:
                if _decrypt_(name_email, user._name):
                    if user._blocked == 0:
                        user._name = name_email
                        for pas in Password.find_all_from_db():
                            if _decrypt_(name_email, pas._username):
                                if Password.confirm_password(password, name_email):
                                    if _decrypt_(password, pas._current_password):
                                        session.update(name_email=user._name)

                                        flash(f'Welcome {user._name}', 'danger')
                                        return True
                                    break
                                flash(f'Password Security Protocol has Updated.\n'
                                      f'Change you Password Please!', 'danger')

            flash('User not Exists\nor\nPassword dont meet complexity!',
                  'danger')

        except Exception:
            flash('Invalid Inputs', 'danger')

    def register(self, username: str, email: str, password: str) -> bool:
        try:
            users = User.find_all_from_db()
            exists = False
            for user in users:
                if _decrypt_(username, user._name):
                    exists = True
            if not exists:
                if Password.confirm_password(password, update=False):
                    user = User(username, email, 0)
                    user.save_to_db(password)

                    flash("Successful Registration", "danger")
                    return True

            flash('Password dont meet complexity!', 'danger')

        except Exception:
            flash('Invalid Inputs', 'danger')

    def change_password(self, username: str, email: str, password: str) -> bool:
        try:
            users = User.find_all_from_db()
            for user in users:
                if _decrypt_(username, user._name):
                    if Password.confirm_password(password, username, update=True):
                        Password._update_to_db(username,
                                               password)
                        flash('Password Changed!', 'danger')
                        return True

            flash('User not Exists\nor\nPassword dont meet complexity!',
                  'danger')

        except Exception as e:
            flash('Invalid Inputs', 'danger')

    def logout(self):
        if session['name_email']:
            flash(f"Goodbye {session['name_email']}", 'danger')
            session['name_email'] = None
