from django.shortcuts import render, HttpResponse

from . import search
from . import forms


# Create your views here.

def search_home(request):
    if request.method == "POST":

        form = forms.SearchForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            url = form.cleaned_data['url']
            laywers = form.cleaned_data['laywers']
            print(search.search(password, url, laywers))


    else:
        form = forms.SearchForm()

    context = {
        "form": form
    }

    return render(request, 'buscador_app/home.html', context)
