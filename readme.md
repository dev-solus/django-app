part 1
sudo apt install python3

python -m venv venv

source activate

pip install django

python -m django --version

django-admin startproject mysite

python manage.py migrate

python manage.py runserver

python manage.py startapp pages

python manage.py makemigrations pages

python manage.py migrate

python manage.py createsuperuser

djm2x
djm2x@hotmail.com
123

git config --global user.email "mohamed-mourabit@digitransform.co"
  git config --global user.name "mohamed.mourabit"