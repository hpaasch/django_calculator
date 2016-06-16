from django import forms

action_choices = (
    ('Add', '+'),
    ('Subtract', '-'),
    ('Multiply', 'x'),
    ('Divide', '/'),
     )


class Calculation(forms.Form):
    entry_one = forms.FloatField(label='Enter one number')
    do_math = forms.ChoiceField(action_choices, label='Choose an operator', required=True)
    entry_two = forms.FloatField(label='Enter another number')



