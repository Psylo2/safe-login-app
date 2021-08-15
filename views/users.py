from flask import Blueprint, url_for, render_template, redirect

from forms.user_forms import LoginForm, RegisterForm, ChangePassForm
import logic.user_logic as UserLogic

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_get():
    form = LoginForm()

    if form.validate_on_submit():
        UserLogic._login(form.name_email.data,
                         form.password.data)

    return render_template('user/login.html', form=form)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_get():
    form = RegisterForm()

    if form.validate_on_submit():
        UserLogic._register(form.username.data,
                            form.email.data,
                            form.password.data)

    return render_template('user/register.html', form=form)


@user_blueprint.route('/change_password', methods=['GET', 'POST'])
def change_password_get():
    form = ChangePassForm()

    if form.is_submitted():
        UserLogic._change_password(form.username.data,
                                   form.password.data)

    return render_template('user/change_password.html', form=form)


@user_blueprint.get('/logout')
def logout():
    UserLogic.logout()

    return redirect(url_for('home'))
