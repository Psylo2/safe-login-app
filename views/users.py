from flask import Blueprint, url_for, render_template, redirect, flash

from forms.user_forms import LoginForm, RegisterForm, ChangePassForm


user_blueprint = Blueprint('users', __name__)
user_blueprint.handler = None


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_get():
    form = LoginForm()

    if form.validate_on_submit():
        result = user_blueprint.handler.login(form.name_email.data,
                                              form.password.data)
        if result:
            return redirect(url_for('home'))
        return login_get()

    return render_template('user/login.html', form=form)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_get():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.password.data == form.re_password.data:
            result = user_blueprint.handler.register(form.username.data,
                                                     form.email.data,
                                                     form.password.data)
            if result:
                return login_get()
            return register_get()

        else:
            flash("passwords not match", ' danger')

    return render_template('user/register.html', form=form)


@user_blueprint.route('/change_password', methods=['GET', 'POST'])
def change_password_get():
    form = ChangePassForm()

    if form.is_submitted():
        result = user_blueprint.handler.change_password(form.username.data,
                                                        form.email.data,
                                                        form.password.data)
        if result:
            return redirect(url_for('users.login_get'))
        return redirect(url_for('users.change_password_get'))

    return render_template('user/change_password.html', form=form)


@user_blueprint.get('/logout')
def logout():
    user_blueprint.handler.logout()
    return redirect(url_for('home'))
