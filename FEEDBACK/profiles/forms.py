from django import forms

class ProfileForm(forms.Form):
    user_image=forms.ImageField()
    # user_image=forms.FileField()
    # user_name=forms.CharField(max_length=100)