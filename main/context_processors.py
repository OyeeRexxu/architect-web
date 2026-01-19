from .models import Service, SiteSettings

def footer_services(request):
    """
    Context processor to make services available in the footer globally.
    """
    services = Service.objects.all().order_by('order')
    settings = SiteSettings.load()
    return {
        'footer_services': services, 
        'global_services': services,
        'global_site_settings': settings,
        'phone_number': settings.phone_number,
        'email': settings.email,
    }
