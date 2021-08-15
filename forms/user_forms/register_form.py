import re
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from models.password import Password


class RegisterForm(FlaskForm):
    username = StringField('Username',
                           render_kw={"class": "contactus__inner-item contactus__inner-username data",
                                      "type": "text",
                                      "autocomplete": "on",
                                      "placeholder": "Username"},
                           validators=[validators.DataRequired(
                               message='Your Username is required')])

    def validate_username(self, field):
        username_matcher = re.compile(r"^[A-Za-z0-9{2,}]+$")
        if not username_matcher.match(field.data):
            raise ValidationError('Invalid credentials for Username')

    email = StringField('Email',
                        render_kw={"class": "contactus__inner-item contactus__inner-email data",
                                   "type": "email",
                                   "autocomplete": "on",
                                   "placeholder": "Email"},
                        validators=[validators.DataRequired(
                            message='Your Email is required'),
                        ])

    def validate_email(self, field):
        email_matcher = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        if not email_matcher.match(field.data):
            raise ValidationError('Invalid credentials for Email')

    password = StringField('Password',
                           render_kw={"class": "contactus__inner-item contactus__inner-password data",
                                      "type": "password",
                                      "autocomplete": "on",
                                      "placeholder": "Password"},
                           validators=[validators.DataRequired(
                               message='Your Password is required')])

    def validate_password(self, field):
        if not Password.confirm_password(field.data):
            raise ValidationError('Password dont meet complex')

    re_password = StringField('re-Password',
                              render_kw={"class": "contactus__inner-item contactus__inner-re_password data",
                                         "type": "password",
                                         "autocomplete": "on",
                                         "placeholder": "re-Password"},
                              validators=[validators.DataRequired(
                                  message='Your re-Password is required'),
                                  validators.EqualTo(
                                      fieldname=password,
                                      message='Password & re-Password dont match')])

    def validate_re_password(self, field):
        if not Password.confirm_password(field.data):
            raise ValidationError('re-Password dont meet complex')
