import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construct_site.settings')
django.setup()

from main.models import Service, ServiceImage

def seed_gallery():
    service = Service.objects.first()
    if not service:
        print("No services found.")
        return

    # Clear existing images for clean test
    ServiceImage.objects.filter(service=service).delete()

    print(f"Adding test images for service: {service.title}")

    # Add 3 test images using available static files
    images = [
        'construction_workspace.png',
        'hero_side_visual.png',
        'hero_split_screen.png'
    ]

    for i, img_path in enumerate(images):
        ServiceImage.objects.create(
            service=service,
            image=img_path,
            caption=f"Test Image {i+1}",
            order=i
        )
        print(f"Added {img_path}")

    print("Done! Check the service detail page.")

if __name__ == '__main__':
    seed_gallery()
