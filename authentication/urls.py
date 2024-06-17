from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile, name='profile'),
    path('profile/categories', profile_category, name='profile_categories'),
    path('profile/delete_category/<int:id_category>', delete_category, name='profile_delete_category')
]