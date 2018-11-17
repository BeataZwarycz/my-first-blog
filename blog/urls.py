from django.urls import path
from . import views

#dodajemy wzorzec adresu URL:
urlpatterns = [
    path('', views.post_list, name='post_list'),
]