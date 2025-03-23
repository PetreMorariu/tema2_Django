from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("api/names", views.name_list, name='name_list'),
    path("api/ages", views.age_list, name='age_list'),
    path("api/combined", views.combine_name_with_age, name='combine_name_with_age'),
    path("api/of_age", views.person_of_age, name='person_of_age'),
]