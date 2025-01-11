from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Account
from django import forms


class Signupform(UserCreationForm):
    class Meta:
        model=Account
        fields=['username','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={     
                'class': 'inputs',              
                'placeholder': 'نام کاربری'         
            }),
            'email': forms.EmailInput(attrs={           
                'class': 'inputs',
                'placeholder': 'ایمیل'
            }),

            # این روش جواب ندا چون استایل دادن به پیشفرض های متا متفاوته
            # 'password1':forms.PasswordInput(attrs={            
            # 'class': 'inputs',
            # 'placeholder': 'رمز عبور'
            # }),
            # 'password2':forms.PasswordInput(attrs={
            # 'class': 'inputs',
            # 'placeholder': 'تأیید رمز عبور'
            # })
            }

    # (سینتکس جنگو) برای فیلدهای پسورد باید جداگانه تعریف بشن
    password1 = forms.CharField(
        label='رمز عبور',                              
        widget=forms.PasswordInput(attrs={             
            'class': 'inputs',
            'placeholder': 'رمز عبور'
        })
    )

    password2 = forms.CharField(
        label='تأیید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'inputs',
            'placeholder': 'تأیید رمز عبور'
        })
    )