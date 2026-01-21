import os
import sys
import django
from django.core.management import call_command

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construct_site.settings')
django.setup()

output_file = 'cms_data.json'

print(f"Exporting data to {output_file} with UTF-8 encoding...")

with open(output_file, 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'main', indent=2, stdout=f)

print(f"Success! {output_file} has been fixed and is ready.")
