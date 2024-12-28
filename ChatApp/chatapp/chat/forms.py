from django import forms
from . models import chatGroup, Usergroup

class chatGroupForm(forms.ModelForm):
    class Meta:
        model = chatGroup
        fields = ['name', 'description']