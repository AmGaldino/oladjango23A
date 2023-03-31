from django.urls import path

from . import views

urlpatterns = [
    path('', view.index, nome='index'),
    path('musica1', view.caneta, nome='caneta'),
]
