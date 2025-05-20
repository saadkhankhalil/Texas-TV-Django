
from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from texas.models import *
from django.http import HttpResponse
import json

# Create your views here.
# This is the Landing Page Logic
def index(request):
    about_feature = AboutFeature.objects.all()
    swip = CheckoutImage.objects.all()
    items = AccordingItem.objects.all()
    testimonials =  Testimonial.objects.all()
    print("Features:", about_feature)
    print("Images:", swip)
    print("Items:", items)
    print("testimonials:", testimonials)

    data = {
        'about_feature': about_feature,
        'swip': swip,
        'items': items,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', data)


def admin_base(request):
    return render(request,'admin_base.html')

# Add About Feature
def add_about_feature(request):
    msg = ''
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        icon = request.FILES.get('icon')
        if title and description and icon:
            AboutFeature.objects.create(title=title, description=description, icon=icon)
            msg = 'About Feature added successfully!'
        else:
            msg = 'Please fill all fields!'
    return render(request, 'add_about.html',{'msg':msg})

# View About Features
def view_about_feature(request):
    about_features = AboutFeature.objects.all()  # Use plural for clarity
    return render(request, 'view_about.html', {'about_features': about_features})



# Update About Feature
def update_about_feature(request, id):
    about_feature = get_object_or_404(AboutFeature, id=id)
    msg = ''
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        icon = request.FILES.get('icon')
        if title and description and icon:
            about_feature.title = title
            about_feature.description = description
            about_feature.icon = icon
            about_feature.save()
            return redirect('view_about')  # Corrected here
        else:
            msg = "Please fill all fields!"
    return render(request, 'update_about.html', {'about_feature': about_feature, 'msg': msg})


# Delete About Feature
def delete_about_feature(request, id):
    about_feature = get_object_or_404(AboutFeature, id=id)
    about_feature.delete()
    return redirect('view_about')  # Corrected here

# Swipe Images
def swipe_images(request):
    msg = ''
    if request.method == 'POST':
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        image = request.FILES.get('image')
        if image:
            CheckoutImage.objects.create(image=image)
            msg = 'Swipp image added successfully!'
        else:
            msg = 'Please fill all fields!'
    return render(request, 'checkout.html', {'msg': msg})







