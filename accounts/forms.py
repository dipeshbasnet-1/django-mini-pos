from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def __init__(self, *args, **kwargs):  # Called automatically when RegisterForm() is created
        super().__init__(*args, **kwargs)  # Create the default UserCreationForm fields
        common_classes = (
            "w-full border border-gray-300 rounded-lg px-4 py-3 "
            "focus:outline-none focus:ring-2 focus:ring-blue-500 "
            "focus:border-blue-500"
        )
        self.fields["username"].widget.attrs.update({
            "class": common_classes,
            "placeholder": "Enter your username"
        })
        self.fields["email"].widget.attrs.update({
            "class": common_classes,
            "placeholder": "Enter your email"
        })
        self.fields["password1"].widget.attrs.update({
            "class": common_classes,
            "placeholder": "Enter your password"
        })
        self.fields["password2"].widget.attrs.update({
            "class": common_classes,
            "placeholder": "Confirm your password"
        })
        
class LoginForm (AuthenticationForm):
    username= forms.CharField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-lg px-4 py-3 " "focus:outline-none focus:ring-2 focus:ring-blue-500 " "focus:border-blue-500",
            "placeholder": "Enter your username"
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-lg px-4 py-3 " "focus:outline-none focus:ring-2 focus:ring-blue-500 " "focus:border-blue-500",
            "placeholder": "Enter your password"
        })
    )