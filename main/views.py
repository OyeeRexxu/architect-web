from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Service
import os

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

def demo_service(request):
    """Demo service page"""
    return render(request, 'demo_service.html')

def backup_files(request):
    """Display list of all backup template files and variant page links"""
    backup_dir = os.path.join(settings.BASE_DIR, 'templates', 'backup')
    backup_files = []
    
    if os.path.exists(backup_dir):
        for filename in os.listdir(backup_dir):
            if filename.endswith('.html'):
                filepath = os.path.join(backup_dir, filename)
                file_stat = os.stat(filepath)
                backup_files.append({
                    'name': filename,
                    'display_name': filename.replace('_', ' ').replace('.html', '').title(),
                    'size': f"{file_stat.st_size / 1024:.1f} KB",
                    'path': f'backup/{filename}'
                })
    
    # Variant page links
    variant_pages = [
        {'name': 'Design Variants', 'url': 'design_variants'},
        {'name': 'Service Variants', 'url': 'service_variants'},
        {'name': 'Service Variants Animated', 'url': 'service_variants_animated'},
        {'name': 'Demo Service', 'url': 'demo_service'},
        {'name': 'Service Detail Variants', 'url': 'service_detail_variants'},
        {'name': 'Footer Variants', 'url': 'footer_variants'},
        {'name': 'Hero Variants', 'url': 'hero_variants'},
        {'name': 'Service Header Variants', 'url': 'service_header_variants'},
        {'name': 'Software Variants', 'url': 'software_variants'},
        {'name': 'About Intro Variants', 'url': 'about_intro_variants'},
        {'name': 'Vertical Slice Variants', 'url': 'vertical_slice_variants'},
    ]
    
    context = {
        'backup_files': backup_files,
        'variant_pages': variant_pages
    }
    return render(request, 'backup_list.html', context)
