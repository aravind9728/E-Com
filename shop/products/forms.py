from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField,BooleanField,TextAreaField,validators,Form

class AddProducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    discount = IntegerField('Discount',default=0)
    stock = IntegerField('Stock',[vaidators.DataRequired()])
    description = IntegerField('Description',[vaidators.DataRequired()])
    colors = TextAreaField('Clors',[validators.DataRequired()])

    image_1 = FileRequired('Image 1', validators =[FileRequired(), FileAllowed('jpg','png','jpeg']), 'image only'])
    image_2 = FileRequired('Image 2', validators =[FileRequired(), FileAllowed('jpg','png','jpeg']), 'image only'])
    image_3 = FileRequired('Image 3', validators =[FileRequired(), FileAllowed('jpg','png','jpeg']), 'image only'])

