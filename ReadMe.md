# Project Octopus

To find out more about Project Octopus, start with the Documentations folder. The Website folder contains the public-facing information. This folder contains the code for working versions of parts of the site. All help creating working versions of the site are very welcome. If you'd like to contribute, please contact alex.freeman@maths.cam.ac.uk


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
