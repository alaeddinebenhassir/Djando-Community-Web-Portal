from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='****************')
    last_name = forms.CharField(max_length=30, required=False, help_text='************')
    email = forms.EmailField(max_length=254, help_text='comentair')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PostForm(forms.ModelForm):
    class Meta :
        model = Post 
        fields = ('title','descreption','text')

class search(forms.ModelForm):
    word = forms.CharField(max_length=30, required=False)
    class Meta :
        fields = ('word',)
        