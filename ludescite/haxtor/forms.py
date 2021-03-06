from django import forms
from django.contrib.auth.models import User
from haxtor.models import UserProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),)
    
    class Meta():
        model = User
        fields= ('username','email','password')
    
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields =('uID','userCat',)


