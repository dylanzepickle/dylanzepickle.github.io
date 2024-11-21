from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='gallery'),
    path('gallery', views.gallery, name='gallery')
]

urlpatterns += staticfiles_urlpatterns()