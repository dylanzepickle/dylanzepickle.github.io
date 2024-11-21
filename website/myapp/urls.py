from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('faq', views.faq, name='faq'),
]

urlpatterns += staticfiles_urlpatterns()