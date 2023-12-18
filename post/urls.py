from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Home-page'),
    path('<int:post_id>/', detail, name='Detail')
]