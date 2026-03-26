from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
        }),
        label='Email Address'
    )

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email is already registered! Please use a different email.'
            )
        return email

    def save(self, commit=True):
        user       = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user