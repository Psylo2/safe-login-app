import re
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError, BooleanField


class PassConfForm(FlaskForm):
    length = StringField('Length',
                         render_kw={"class": "contactus__inner-item contactus__inner-length data",
                                    "type": "number",
                                    "autocomplete": "on",
                                    "placeholder": "Password Length"},
                         validators=[validators.DataRequired(
                             message='Password Length is required')])

    def validate_length(self, field):
        _matcher = re.compile(r"[0-9]")
        if not _matcher.match(field.data):
            raise ValidationError('Invalid credentials for Length')

    upper = BooleanField("A-Z",
                         render_kw={"class": "form__inner-wrapper1",
                                    "type": "checkbox",
                                    "value": 'true',
                                    "checked": "true"},
                         false_values='false')

    lower = BooleanField("a-z",
                         render_kw={"class": "form__inner-wrapper2",
                                    "type": "checkbox",
                                    "value": 'true',
                                    "checked": "true"},
                         false_values='false')

    digits = BooleanField("0-9",
                          render_kw={"class": "form__inner-wrapper3",
                                     "type": "checkbox",
                                     "value": 'true',
                                     "checked": "true"},
                          false_values='false')

    spec = BooleanField("!@#$%^&*_+.,",
                        render_kw={"class": "form__inner-wrapper4",
                                   "type": "checkbox",
                                   "value": 'true',
                                   "checked": "true"},
                        false_values='false')

    history = StringField('History',
                          render_kw={"class": "contactus__inner-item contactus__inner-history data",
                                     "type": "number",
                                     "autocomplete": "on",
                                     "placeholder": "Password History"},
                          validators=[validators.DataRequired(
                              message='Password History is required')])

    def validate_history(self, field):
        _matcher = re.compile(r"^[0-9]{1,10}$")
        if not _matcher.match(field.data):
            raise ValidationError('Invalid credentials for Length')

    use_dict = BooleanField("[...]",
                            render_kw={"class": "form__inner-wrapper5",
                                       "type": "checkbox",
                                       "value": 'false'},
                            false_values='true')

    tries = StringField('Tries',
                        render_kw={"class": "contactus__inner-item contactus__inner-tries data",
                                   "type": "number",
                                   "autocomplete": "on",
                                   "placeholder": "Password fail attempts"},
                        validators=[validators.DataRequired(
                            message='Password fail attempts is required')])

    def validate_tries(self, field):
        _matcher = re.compile(r"^[1-9]$")
        if not _matcher.match(field.data):
            raise ValidationError('Invalid credentials for Length')
