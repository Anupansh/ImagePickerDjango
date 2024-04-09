from django import forms


class upload_File_form(forms.Form):
    file = forms.FileField()
