import os
from django.conf import settings
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gallery(request):
    # path to image directory
    images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')

    # list all image files
    images = [f'images{file}' for file in os.listdir(images_dir) if file.endswith(('.jpg', '.png'))]

    return render(request, 'gallery.html')