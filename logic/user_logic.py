from flask import url_for, redirect, flash, session
from models.user import User
from models.password import Password


def _login(name_email: str, password: str):
    try:
        user = User.find_from_db(name_email)
        user_pas = Password.find_from_db(name=user._name)

        if user and user_pas._current_password == password:
            session.update(name_email=user._name)

            flash(f'Welcome {user._name}', 'danger')
            return redirect(url_for('home'))

        flash('User not Exists\nor\nPassword dont meet complexity!',
              'danger')

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')

    return redirect(url_for('users.login_get'))


def _register(username: str, email: str,
              password: str):
    try:
        user = User(username, email, 0)
        user.save_to_db()
        pas = Password(username=user._name)

        if pas.confirm_password(password):
            pas._current_password = password
            pas.save_to_db()

            flash("Successful Registration", "danger")
            return redirect(url_for('users.login_get'))

        flash('Password dont meet complexity!', 'danger')

    except Exception as e:
        print(e)
    flash('Invalid Inputs', 'danger')

    return redirect(url_for('users.register_get'))


def _change_password(username: str, password: str):
    try:
        user = User.find_from_db(username)

        if user:
            new_passw = Password(username=username)

            if new_passw.confirm_password(password):
                new_order = new_passw.order_new_password(
                    username=user._name,
                    password=password)

                new_passw.update_to_db(new_order)
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
