from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="Post title",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    pre_post = StringField(
        label="Greetings"
    )
    post = TextAreaField(
        label="Post text",
        validators=[
            DataRequired()
        ]
    )
