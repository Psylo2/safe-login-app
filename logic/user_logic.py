from flask import url_for, redirect, flash, session
from models.user import User
from models.password import Password
from db.db import _decrypt_


def _login(name_email: str, password: str):
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
                                    return redirect(url_for('home'))
                                break
                            flash(f'Password Security Protocol has Updated.\n'
                                  f'Change you Password Please!', 'danger')
                            return redirect(url_for('users.change_password_get'))

        flash('User not Exists\nor\nPassword dont meet complexity!',
              'danger')

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')

    return redirect(url_for('users.login_get'))


def _register(username: str, email: str,
              password: str):
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
                return redirect(url_for('users.login_get'))

        flash('Password dont meet complexity!', 'danger')

    except Exception as e:
        print(e)
    flash('Invalid Inputs', 'danger')

    return redirect(url_for('users.register_get'))


def _change_password(username: str, email: str, password: str):
    try:
        users = User.find_all_from_db()
        for user in users:
            if _decrypt_(username, user._name):
                if Password.confirm_password(password, username, update=True):
                    Password._update_to_db(username,
                                           password)
                    flash('Password Changed!', 'danger')
                    return redirect(url_for('users.login_get'))
        flash('User not Exists\nor\nPassword dont meet complexity!',
              'danger')

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')

    return redirect(url_for('users.change_password_get'))


def logout():
    if session['name_email']:
        flash(f"Goodbye {session['name_email']}", 'danger')
        session['name_email'] = None
