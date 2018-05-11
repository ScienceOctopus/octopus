create a virtualenv

git clone https://github.com/arkain/octopus.git

pip install -r requirements.txt

python manage.py migrate

./manage.py loaddata db_export.json

python manage.py runserver

Navigate to 127.0.0.1:8000