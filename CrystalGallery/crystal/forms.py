from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Listing
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'username', 'nickname')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth',
                  'is_active', 'is_admin', 'username', 'nickname')

    def clean_password(self):
        return self.initial["password"]

#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
        'name',
        'initial',
        'user',
        'display_picture',
        'explain',
        ]