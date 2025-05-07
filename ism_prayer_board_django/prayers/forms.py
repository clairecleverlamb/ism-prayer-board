from django import forms
from .models import PrayerRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['student_name', 'ministry_group', 'status', 'content']
        labels = {
            'student_name': 'Name',
            'ministry_group': 'Mentor',
            'status': 'Status',
            'content': 'Prayer Request',
        }
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control border border-secondary rounded px-3 py-2'}),
            'ministry_group': forms.TextInput(attrs={'class': 'form-control border border-secondary rounded px-3 py-2'}),
            'status': forms.TextInput(attrs={'class': 'form-control border border-secondary rounded px-3 py-2'}),
            'content': forms.Textarea(attrs={'class': 'form-control border border-secondary rounded px-3 py-2', 'rows': 3}),
        }

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Acts2 Email'
    }))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2'] 

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@acts2.network'):
            raise forms.ValidationError("Only Acts2 Network emails allowed.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        user.username = email  
        user.email = email
        if commit:
            user.save()
        return user

class CustomSigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control border border-dark rounded px-3 py-2',
            'placeholder': 'Your Acts2 email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control border border-dark rounded px-3 py-2',
            'placeholder': 'Your password'
        })
