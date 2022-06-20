from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=3)
        ]
    )
    password = StringField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, max=255)
        ]
    )
    logged_in = BooleanField(
        label="I'm sure",
        name="logged-in"
    )
