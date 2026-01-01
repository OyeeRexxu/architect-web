from .models import Service

def footer_services(request):
    """
    Context processor to make services available in the footer globally.
    """
    services = Service.objects.all().order_by('order')
    return {'footer_services': services, 'global_services': services}
