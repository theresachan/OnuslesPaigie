from wtforms.fields import *
from wtforms.fields.html5 import EmailField
from wtforms import Form, StringField, TextAreaField, validators, SelectField, IntegerField

class CreateEntryForm(Form):
    cost_category = StringField('Cost Category', [validators.Length(min=1, max=150), validators.DataRequired()])
    expenses = StringField('Expenses', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Optional()])

class CheckoutForm(Form):
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email', [validators.DataRequired()])
    phone = IntegerField('Phone Number', [validators.DataRequired()])
    country = SelectField('Country', [validators.DataRequired()],
                         choices=[('', 'Select'), ('S', 'Singapore'), ('AF', 'Afghanistan')], default='')
    address1 = StringField('Address Line 1', [validators.DataRequired()])
    address2 = StringField('Address Line 2', [validators.DataRequired()])
    postal_code = IntegerField('Postal Code', [validators.DataRequired()])

    card_name = StringField("Card Name", [validators.Optional()])
    card_number = IntegerField("Card Number", [validators.Optional()])
    expiry_date = DateTimeField("Expiry Date", [validators.Optional()])
    cvv = IntegerField("CVV", [validators.Optional()])
    remember_me = BooleanField("Remember Me")



