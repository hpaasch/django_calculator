from django import forms

action_choices = (
    ('Add', '+'),
    ('Subtract', '-'),
    ('Multiply', '*'),
    ('Divide', '/'),
     )


class Calculation(forms.Form):
    entry_one = forms.FloatField()  # change this to TextInput???
    do_math = forms.ChoiceField(action_choices, required=True)
    entry_two = forms.FloatField()



