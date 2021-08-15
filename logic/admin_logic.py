from flask import request, url_for, redirect, flash, render_template, session

from logic.user_logic import Password
from models.user import User


def users_list():
    _users = User.find_all_from_db()
    return render_template('admin/user_list.html', users=_users)


def block_user(block):
    user = User.find_from_db(block)
    user.block_user_model()


def unblock_user(unblock):
    user = User.find_from_db(unblock)
    user.unblock_user_model()


def password_configuration(upper: bool, lower: bool, digits: bool,
                           spec: bool, use_dict: bool, length: str,
                           history: str, tries: str):
    re = ""
    try:
        re += "A-Z" if upper else ""
        re += "a-z" if lower else ""
        re += "0-9" if digits else ""
        re += "\!\#\$\%\^\&\*\_\+\.\," if spec else ""


        Password._set_config(length=length,
                             regex=re,
                             history=history,
                             dictionary=use_dict,
                             tries=tries)


        flash('Password Configuration Changed!', 'danger')

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
    return redirect(url_for('admin.password_conf_get'))
