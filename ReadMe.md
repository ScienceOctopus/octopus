git clone https://github.com/arkain/octopus.git

pip install -r requirements.txt

python manage.py migrate

./manage.py loaddata db_export.json