from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

#creating fields for form and ensuring each of the fields informtion is validated
class ContactForm(FlaskForm):
    name= StringField("Name", validators=[DataRequired(), Length (max=75)])
    email= StringField("Email", validators=[DataRequired(), Email(), Length(max=90)])
    subject= StringField("Subject", validators=[DataRequired(), Length(max=60)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10,max=2550)])
    submit= SubmitField("Send")