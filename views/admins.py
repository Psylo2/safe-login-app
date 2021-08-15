from flask import Blueprint, render_template, redirect, url_for

from forms.admin_forms import PassConfForm
import logic.admin_logic as AdminLogic
from models.user.decorator import requires_admin

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/password_config', methods=['GET', 'POST'])
@requires_admin
def password_conf_get():
    form = PassConfForm()

    if form.validate_on_submit():
        AdminLogic.password_configuration(upper=form.upper.data, lower=form.lower.data,
                                          digits=form.digits.data, spec=form.spec.data,
                                          use_dict=form.use_dict.data, length=form.length.data,
                                          history=form.history.data, tries=form.tries.data)

    return render_template('admin/password_config.html', form=form)

@admin_blueprint.get('/menu')
@requires_admin
def menu_get():
    return render_template('admin/menu.html')

@admin_blueprint.get('/all_users')
@requires_admin
def all_users_get():
    return AdminLogic.users_list()

@admin_blueprint.get('/block/<string:block>')
@requires_admin
def block_user(block):
    AdminLogic.block_user(block)
    return redirect(url_for('admin.all_users_get'))

@admin_blueprint.get('/unblock/<string:unblock>')
@requires_admin
def unblock_user(unblock):
    AdminLogic.unblock_user(unblock)
    return redirect(url_for('admin.all_users_get'))
