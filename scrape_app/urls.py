from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('find_pic', views.find_pic),
    path('display_pic', views.display_pic)
]
