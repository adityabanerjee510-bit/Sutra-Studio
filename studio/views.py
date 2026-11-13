from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at the sutra_studio's home page...")
    return render(request, 'webpages/index.html')

# def about(request):
#     return render(request, 'website/about.html')

# def contact(request):
#     return render(request, 'website/contact.html')