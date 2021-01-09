from wtforms import Form, StringField, validators

class CreateEntryForm(Form):
    cost_category = StringField('Cost Category', [validators.Length(min=1, max=150), validators.DataRequired()])
    expenses = StringField('Expenses', [validators.Length(min=1, max=150), validators.DataRequired()])
