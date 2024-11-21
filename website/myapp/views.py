import os
from django.conf import settings
from django.shortcuts import render, HttpResponse

image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gallery(request):
    # path to image directory
    images_dir = os.path.join(settings.BASE_DIR, 'myapp', 'assets', 'images', 'gallery')
    print(f'Image directory: {images_dir}')

    image_list = [
        f'images/gallery/{filename}' for filename in os.listdir(images_dir) if filename.lower().endswith(image_extensions)
    ]
    print(f'Image list:\n{image_list}')

    return render(request, 'gallery.html', {'images': image_list})

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

