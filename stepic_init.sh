sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database project_db;"
mysql -uroot -e "grant all privileges on project_db.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf.py ask.wsgi:application

