from django.urls import path
from backend.urls import urlpatterns
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("api/names", views.name_list, name='name_list')
]