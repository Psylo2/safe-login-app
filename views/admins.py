from flask import Blueprint, render_template, redirect, url_for

from forms.admin_forms import PassConfForm
from models.user.decorator import requires_admin

admin_blueprint = Blueprint('admin', __name__)
admin_blueprint.handler = None


@admin_blueprint.route('/password_config', methods=['GET', 'POST'])
@requires_admin
def password_conf_get():
    form = PassConfForm()

    if form.validate_on_submit():
        result = admin_blueprint.handler.password_configuration(upper=form.upper.data, lower=form.lower.data,
                                                                digits=form.digits.data, spec=form.spec.data,
                                                                use_dict=form.use_dict.data, length=form.length.data,
                                                                history=form.history.data, tries=form.tries.data)

        if result:
            return render_template('admin/password_config.html', form=form)
        return password_conf_get()


@admin_blueprint.get('/menu')
@requires_admin
def menu_get():
    return render_template('admin/menu.html')


@admin_blueprint.get('/all_users')
@requires_admin
def all_users_get():
    try:
        all_users = admin_blueprint.handler.users_list()
        return render_template('admin/user_list.html', users=all_users)
    except Exception:
        return menu_get()


@admin_blueprint.get('/block/<string:block>')
@requires_admin
def block_user(block):
    result = admin_blueprint.handler.block_user(block)
    if result:
        return redirect(url_for('admin.all_users_get'))
    return menu_get()


@admin_blueprint.get('/unblock/<string:unblock>')
@requires_admin
def unblock_user(unblock):
    result = admin_blueprint.handler.unblock_user(unblock)
    if result:
        return redirect(url_for('admin.all_users_get'))
    return menu_get()
