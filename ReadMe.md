# Project Octopus

# Installation instructions

Create a virtualenv and then:


```bash
git clone https://github.com/octopus-hypothesis/octopus.git
pip install -r requirements.txt
python manage.py migrate
./manage.py loaddata db_export.json
python manage.py runserver
```

Navigate to 127.0.0.1:8000
