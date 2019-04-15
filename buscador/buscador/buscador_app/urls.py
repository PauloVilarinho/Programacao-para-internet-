from django.urls import path

from . import views

app_name = 'buscador_app'

urlpatterns = [
    path('', views.search_home, name='home')

]