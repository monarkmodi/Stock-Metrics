from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class StockForm(forms.Form):
    symbol = forms.RegexField(label=_("Symbol"), max_length=5,
        regex=r'^[A-Za-z0-9]+$',
        help_text=_("Required. 5 characters or fewer. Latin letters or digits"),
        error_messages={
            'invalid': _("This value may contain only latin letters or digits"),
        })
    
class AccountForm(forms.Form):
    funds_available = forms.FloatField(label='funds_avilable')
    port_value = forms.FloatField(label='port_value')
    profit_loss = forms.FloatField(label='profit_loss')


class OrderForm(forms.Form):
    symbol = forms.RegexField(label=_("Symbol"), max_length=5,
        regex=r'^[A-Za-z0-9]+$',
        help_text=_("Required. 5 characters or fewer. Latin letters or digits"),
        error_messages={
            'invalid': _("This value may contain only latin letters or digits"),
        })
    shares = forms.RegexField(label=_("Symbol"), max_length=10,
            regex=r'^[0-9]+$',
            help_text=_("Required."),
            error_messages={
                'invalid': _("This value may contain only digits"),
            })