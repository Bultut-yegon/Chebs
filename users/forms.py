from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    profile_pic = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = UserProfile(user=user,profile_pic=self.cleaned_data["profile_pic"])
            profile.save()
        return user