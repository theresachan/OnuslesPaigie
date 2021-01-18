from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
class CreateEntryForm(Form):
    cost_category = StringField('Cost Category', [validators.Length(min=1, max=150), validators.DataRequired()])
    expenses = StringField('Expenses', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateReturnForm(Form):
    product = StringField('Product ID', [validators.Length(min=1, max=150), validators.DataRequired()])
    quantity = SelectField('Quantity', [validators.DataRequired()], choices=[('', 'Select'), ('1', '1'), ('2', '2')], default='')
    reason = RadioField('Select a return reason', choices=
    [('D', 'Damaged or defective item(s)'),
     ('N', 'Not true in size / measurement'),
     ('P', 'Poor quality of fabric / Faulty'),
     ('L', 'Look different / Not as described'),
     ('O', 'Others'), ],
       default='F')

    remarks = TextAreaField('Remarks', [validators.Optional()])
