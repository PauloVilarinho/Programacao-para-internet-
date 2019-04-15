from django import forms


class SearchForm(forms.Form):
    password = forms.CharField()
    url = forms.CharField()
    laywers = forms.IntegerField()


