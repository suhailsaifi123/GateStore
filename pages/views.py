from django.shortcuts import render, redirect, get_object_or_404
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .models import NewsletterSubscriber
from django.core.mail import send_mail
from gates.models import Gate

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def gallery(request):
    # Show only 6 gates in the gallery for better presentation
    gates = Gate.objects.all()[:6]
    return render(request, 'pages/gallery.html', {'gates': gates})

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and not NewsletterSubscriber.objects.filter(email=email).exists():
            NewsletterSubscriber.objects.create(email=email)
            # Send notification to admin
            send_mail(
                'New Newsletter Subscriber',
                f'New subscriber: {email}',
                settings.DEFAULT_FROM_EMAIL,
                ['suhailkhan18053@gmail.com'],
                fail_silently=True,
            )
            return JsonResponse({'success': True, 'message': 'Subscribed successfully!'})
        return JsonResponse({'success': False, 'message': 'Already subscribed or invalid email.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def warranty(request):
    return render(request, 'pages/warranty.html')

def installation(request):
    return render(request, 'pages/installation.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def terms(request):
    return render(request, 'pages/terms.html')

def logo_test(request):
    """Simple view to test logo display"""
    logo_test_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logo_test.html')
    with open(logo_test_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return HttpResponse(content)
