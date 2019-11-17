from django import forms
from .models import *


# class ProfileRegisterForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['email', 'mobileno', 'password', 'hometown', 'city', 'country',
#                   'live_with_family', 'marital_status', 'diet', 'height', 'caste', 'education_level',
#                   'education_field', 'college_name', 'work_with', 'monthly_income']


class ProfileRegisterFormOne(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['email', 'mobileno', 'password', 'confirmPassword']

# fields = ['email', 'mobileno', 'password', 'hometown', 'city', 'country',
#  'live_with_family', 'marital_status','diet', 'height', 'caste', 'education_level',
# 'education_field', 'college_name', 'work_with', 'monthly_income']


class ProfileRegisterFormTwo(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['hometown', 'city', 'country', 'liveWithFamily',
                  'maritalStatus', 'diet', 'height', 'caste', ]


class ProfileRegisterFormThree(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['education_level', 'education_field',
                  'college_name', 'work_with', 'monthly_income', ]
