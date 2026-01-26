@echo off
echo Starting Build Process...

:: Pull latest code
echo Pulling latest code form git...

:: Backup Database
echo Backing up database...
copy db.sqlite3 db.sqlite3.bak

:: Reset DB to match git
git update-index --no-assume-unchanged db.sqlite3
git checkout db.sqlite3

:: Pull
git pull origin main

:: Restore Live Database
echo Restoring live database...
copy /Y db.sqlite3.bak db.sqlite3
del db.sqlite3.bak

:: Install dependencies
echo Installing requirements...
pip install -r requirements.txt

:: Apply Migrations
echo Applying Database Migrations...
python manage.py makemigrations
python manage.py migrate

:: Collect Static Files
echo Collecting Static Files...
python manage.py collectstatic --noinput

echo Build Process Completed Successfully!
pause
