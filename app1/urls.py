from django.urls import path
from . import views
urlpatterns = [
    path('', views.link1, name = 'link1'),
    path('star',views.star, name = 'star'),
]