sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn.conf.py hello:wsgi_application 
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf.py ask.wsgi:application

