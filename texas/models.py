from django.db import models

# Create your models here.
class AboutFeature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='about_icons/')

    def __str__(self):
        return self.title


# Data Base for Swipe images
class CheckoutImage(models.Model):
    image = models.ImageField(upload_to='checkout')


# According Item Data Base
class AccordingItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="CEO, Company")
    text = models.TextField()
    photo = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
