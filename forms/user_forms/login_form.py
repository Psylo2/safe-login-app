import re
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError


class LoginForm(FlaskForm):
    name_email = StringField('Username',
                             render_kw={"class": "contactus__inner-item contactus__inner-username data",
                                        "type": "text",
                                        "autocomplete": "on",
                                        "placeholder": "Username"})

    def validate_name_email(self, field):
        email_matcher = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        if not email_matcher.match(field.data):
            username_matcher = re.compile(r"^[A-Za-z0-9{2,}]+$")
            if not username_matcher.match(field.data):
                raise ValidationError('Invalid credentials for Name/E-mail')

    password = StringField('Password',
                           render_kw={"class": "contactus__inner-item contactus__inner-password data",
                                      "type": "password",
                                      "autocomplete": "on",
                                      "placeholder": "Password"})

