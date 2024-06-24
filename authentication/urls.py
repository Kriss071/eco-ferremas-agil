from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile, name='profile'),
    path('profile/categories', profile_category, name='profile_categories'),
    path('profile/delete_category/<int:id_category>', delete_category, name='profile_delete_category'),
    path('profile/add_product', profile_product, name='profile_product'),
    path('profile/directions', profile_directions, name="profile_directions")
]