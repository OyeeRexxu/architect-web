import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "construct_site.settings")
django.setup()

from main.models import Service, ServiceSection

print("Checking Services...")
for s in Service.objects.all():
    if "Estimation" in s.title or "Software" in s.title:
        print(f"Service: {s.title}")
    
    for sect in s.sections.all():
        if "Software" in sect.heading or "Estimation" in sect.heading:
            print(f"  Section: {sect.heading}")
        if sect.items and ("Software" in sect.items or "Estimation" in sect.items):
             print(f"  Items in {sect.heading}: {sect.items}")
