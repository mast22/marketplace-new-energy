from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import SignupForm

from .models import CustomUser

# class CustomSignupForm(SignupForm):
#     email = forms.CharField(label='Элекстронная почта')
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

#     def signup(self, request, user):
#         if password == repeat_password

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

class PersonRoleForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('entity_name', 'entity_name', 'first_name', 'last_name', 'role', 'person', 'permission', 'staff', 'exp', 'reviews', 'equip')


