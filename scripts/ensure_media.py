import os
import shutil
import sys

# Define base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

def ensure_media():
    print("Running Media Seeding Check...")
    
    # Define mappings: Source (in static) -> Destination (in media)
    # Note: These paths are relative to static/ and media/ roots respectively
    mappings = [
        # Services Header Background
        ('images/services_header_bg.png', 'images/services_header_bg.png'),
        
        # Service Icons/Images (Copy entire folder content logic roughly)
        # But here we specific what we know
        ('images/services/estimation.png', 'services/estimation.png'),
        # Add a directory mapping logic below instead of individual files if possible, 
        # but individual is safer for specific known assets. To be robust, let's do directories.
    ]

    # Directory Mappings: (Source Dir Name in static, Dest Dir Name in media)
    dir_mappings = [
        ('images/services', 'services'),
        ('images/software', 'images/software'),
    ]

    # Create Media Root if not exists
    if not os.path.exists(MEDIA_ROOT):
        os.makedirs(MEDIA_ROOT)
        print(f"Created {MEDIA_ROOT}")

    # Process Directory Mappings
    for src_dir_name, dest_dir_name in dir_mappings:
        src_path = os.path.join(STATIC_ROOT, src_dir_name)
        dest_path = os.path.join(MEDIA_ROOT, dest_dir_name)

        if not os.path.exists(src_path):
            print(f"Warning: Source directory {src_path} does not exist. Skipping.")
            continue

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            print(f"Created directory {dest_path}")

        # Walk through source and copy files if they don't exist in dest
        for root, dirs, files in os.walk(src_path):
            # Compute relative path from src_path
            rel_path = os.path.relpath(root, src_path)
            dest_root = os.path.join(dest_path, rel_path)

            if not os.path.exists(dest_root):
                os.makedirs(dest_root)

            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_root, file)

                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)
                    print(f"Seeded: {dest_file}")
                # else:
                #    print(f"Exists: {dest_file}")

    # Process Individual File Mappings (if any remain outside directories)
    for src_name, dest_name in mappings:
        src_file = os.path.join(STATIC_ROOT, src_name)
        dest_file = os.path.join(MEDIA_ROOT, dest_name)
        
        # Check if src exists
        if not os.path.exists(src_file):
            # Try finding it in the root of static just in case
            continue

        dest_dir = os.path.dirname(dest_file)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        if not os.path.exists(dest_file):
            shutil.copy2(src_file, dest_file)
            print(f"Seeded: {dest_file}")

    print("Media Seeding Completed.")

if __name__ == "__main__":
    ensure_media()
