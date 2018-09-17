from django import forms
from .models import Tinps


class TinpsForm(forms.Form):

    class Meta:
        model = Tinps
        fields = ('title', 'tinps_body')
