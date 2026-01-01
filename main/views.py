from django.shortcuts import render, redirect, get_object_or_404
from .models import Service

def home(request):
    """Home page view with hero section, services, and statistics"""
    services = Service.objects.all()
    context = {
        'stats': [
            {'number': '500+', 'label': 'Projects'},
            {'number': '24-48h', 'label': 'Turnaround'},
            {'number': '98%', 'label': 'Satisfaction'},
            {'number': '50+', 'label': 'Team'},
        ],
        'services': services
    }
    services = Service.objects.all()
    context = {
        'stats': [
            {'number': '500+', 'label': 'Projects'},
            {'number': '24-48h', 'label': 'Turnaround'},
            {'number': '98%', 'label': 'Satisfaction'},
            {'number': '50+', 'label': 'Team'},
        ],
        'services': services
    }
    return render(request, 'home.html', context)

def contact(request):
    """Contact page view"""
    return render(request, 'contact.html')

def portfolio(request):
    """Portfolio/gallery page view"""
    context = {
        'projects': [
            {
                'title': 'Modern Office Complex',
                'category': 'Commercial',
                'image': 'project1.jpg'
            },
            {
                'title': 'Sustainable Residence',
                'category': 'Residential',
                'image': 'project2.jpg'
            },
            {
                'title': 'Urban Park Design',
                'category': 'Landscape',
                'image': 'project3.jpg'
            },
        ]
    }
    return render(request, 'portfolio.html', context)

def about(request):
    """About page view with company information, vision, and mission"""
    return render(request, 'about.html')

def new_home(request):
    """Backup page with old Vision/Mission content"""
    return render(request, 'new_home.html')

def design_variants(request):
    """Design variants demo page"""
    return render(request, 'design_variants.html')

def service_variants(request):
    """Service section design variants demo page"""
    return render(request, 'service_variants.html')

def service_variants_animated(request):
    services = Service.objects.all()[:3]
    context = {
        'services': services
    }
    return render(request, 'service_variants_animated.html', context)

def service_detail_variants(request):
    """5 Variants for Service Detail Page"""
    # Demo with first service from DB
    service = Service.objects.first()
    context = {
        'service': service
    }
    return render(request, 'service_detail_variants.html', context)

def service_detail(request, slug):
    """Service detail page view"""
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all()
    context = {
        'service': service,
        'services': services
    }
    return render(request, 'service_detail.html', context)

def footer_variants(request):
    """5 Variants for Footer Design"""
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'footer_variants.html', context)
