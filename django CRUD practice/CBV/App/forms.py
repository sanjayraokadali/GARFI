from django import forms
from App.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
