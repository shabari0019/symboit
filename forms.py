from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField



class CreatePostForm(FlaskForm):
    q1 = StringField("Q1. Field of Interest. (Software/Hardware)", validators=[DataRequired()])
    q2 = StringField("Q2. Your Age.", validators=[DataRequired()])
    q3 = StringField("Q3. Level of Experience (Beginner/Moderate/Expert)", validators=[DataRequired()])
    q4 = StringField("Q4. Mode of Event (Online/Offline)", validators=[DataRequired()])
    q5 = StringField("Q5. Competitive/Knowledge Based", validators=[DataRequired()])
    title = StringField("Event Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Event Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Event Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    q1 = StringField("Q1. Field of Interest. (Software/Hardware)",validators=[DataRequired()])
    q2 = StringField("Q2. Your Age in years.",validators=[DataRequired()])
    q3 = StringField("Q3. Level of Experience (Beginner/Moderate/Expert)", validators=[DataRequired()])
    q4 = StringField("Q4. Mode of Event (Online/Offline)", validators=[DataRequired()])
    q5 = StringField("Q5. Competitive/Knowledge Based", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
