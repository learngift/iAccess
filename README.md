# My first django project

# python installation
wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
bash Miniconda3-latest-Linux-x86_64.sh  -b  -p  $(pwd)/python
. $(pwd)/python/bin/activate

pip install Django sqlite-web

# checks
python --version

python
import django
django.VERSION

# django commands
django-admin startproject iAccess

cd iAccess
git init . ; git add -A . ; git commit -m "initial commit"

django-admin startapp badgeur # create an application in out project

manage.py runserver 8000 # start a dev server

# create db:
(https://docs.djangoproject.com/fr/4.2/topics/migrations/)
./manage.py makemigrations
./manage.py migrate
sqlite-web db.sqlite3

# readings
[draw.io documentation for uml diagrams](https://drawio-app.com/blog/uml-class-diagrams-in-draw-io/)
[old django tuto in french](https://www.formation-django.fr/framework-django/premier-projet/modeles.html) 


