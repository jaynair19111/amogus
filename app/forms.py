from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class ItemEntry(FlaskForm):
    item = StringField('item')
    category = SelectField(u'Category', choices=[])

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")