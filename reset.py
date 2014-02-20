#!
rm labsoft/labsoft.db
./manage.py syncdb --noinput
./manage.py createsuperuser --username=sa --email=sa@me.org
