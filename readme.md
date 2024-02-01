part 1
sudo apt install python3

python -m venv venv

source activate

pip install django

python -m django --version

django-admin startproject mysite

python manage.py migrate

python manage.py runserver