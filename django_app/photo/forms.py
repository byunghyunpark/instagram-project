from django import forms


class PhotoAddForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput())
