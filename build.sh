#!/bin/bash

echo "Starting Build Process..."

# Activate pythonanywhere virtualenv
source /home/rexxu/venv/bin/activate

# Pull latest code
echo "Pulling latest code form git..."

# Backup Database
echo "Backing up database..."
cp db.sqlite3 db.sqlite3.bak

# Reset DB to match git (allow pull)
git update-index --no-assume-unchanged db.sqlite3 || true
git checkout db.sqlite3

# Pull
git pull origin main

# Restore Live Database
echo "Restoring live database..."
cp db.sqlite3.bak db.sqlite3
rm db.sqlite3.bak

# Install dependencies
echo "Installing requirements..."
pip install Pillow
pip install -r requirements.txt

# Apply Migrations
echo "Applying Database Migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect Static Files
echo "Collecting Static Files..."
python manage.py collectstatic --noinput

echo "Build Process Completed Successfully!"
