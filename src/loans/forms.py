from django import forms

CURRENCY_CHOICES = (
    ('KZT', 'KZT'),
    ('USD', 'USD'),
    ('EUR', 'EUR')
)

TERM_CHOICES = (
    ('1 month', '1'),
    ('3 month', '3'),
    ('6 month', '6'),
    ('9 month', '9'),
    ('1 year', '12'),
    ('1,5 year', '18'),
    ('2 years', '24'),
    ('3 years', '36'),
    ('4 years', '48'),
    ('5 years', '60'),
)

class CreditForm(forms.Form):
    total = forms.CharField(max_length=100)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)
    term = forms.ChoiceField(choices=TERM_CHOICES)
    
