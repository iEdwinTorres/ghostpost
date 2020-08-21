from django import forms
from ghostpost_app.models import BoastRoast


class PostForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ["choices", "user_post"]
