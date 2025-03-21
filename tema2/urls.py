from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("api/names", views.name_list, name='name_list'),
    path("api/ages", views.age_list, name='age_list')
]