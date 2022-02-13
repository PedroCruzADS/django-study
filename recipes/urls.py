from django.urls import path

from recipes.views import _contato, _home, _sobre

urlpatterns = [
    path('', _home),
    path('contato/', _contato),
    path('sobre/', _sobre)
]
