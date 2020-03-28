sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/gunicorn.conf.py
sudo /etc/init.d/gunicorn -c /etc/gunicorn.d/gunicorn.conf.py hello:wsgi_application
