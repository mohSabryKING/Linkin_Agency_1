from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from .models import *
from django import forms

class FormUser(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2',)
    
'''class Profile_creation():
    class Meta:
        model = User_profile
        fields = "__all__"'''


'''class Profile_creation(forms.ModelF):
    class Meta:
        model = User_profile
        fields = "__all__"'''


class Profile_creation_Form(forms.ModelForm):
    class Meta:
        '''
           client_img
           client_name
           contracted_with
           phone_number
        '''
        model = User_profile
        fields = "__all__"
        
