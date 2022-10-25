from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Length, Regexp
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CreateRegisterForm(FlaskForm):
    username = StringField("Username :", validators=[DataRequired()])
    email = EmailField("Email :", validators=[DataRequired()])
    password = PasswordField("Password :", validators=[DataRequired(), Length(min=8), Regexp('^[\w-]+$',
    rep_password = PasswordField("Repeat password :", validators=[DataRequired(),  Length(min=8), Regexp('^[\w-]+$',
                                                                                             message='Username can contain only alphanumeric characters (and _, -).')])
    submit = SubmitField("Sign up")


class LoginUser(FlaskForm):
    email = StringField("Email :", validators=[DataRequired()])
    password = PasswordField("Password :", validators=[DataRequired(), Length(min=8), Regexp('^[\w-]+$',
                                                                                             message='Username can contain only alphanumeric characters (and _, -).')])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    content = CKEditorField("Add a comment:", validators=[DataRequired()])
    submit = SubmitField("Add")
