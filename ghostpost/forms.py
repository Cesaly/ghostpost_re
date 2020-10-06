from django import forms


class newPost(forms.Form):
    is_boast = forms.BooleanField(required=True)
    content = forms.CharField(max_length=200)
