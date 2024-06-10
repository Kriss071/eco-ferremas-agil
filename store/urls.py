from django.urls import path
from store import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('catalogue', v.catalogue, name='catalogue')
]