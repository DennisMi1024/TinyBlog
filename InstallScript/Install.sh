#/bin/bash
#This file is writen by Dennis Mi to Install django_blog
apt-get update
export LC_ALL=C
apt-get install git
mkdir MyBlog
cd MyBlog
git clone https://github.com/lzjun567/django_blog
apt-get install python-pip
apt-get install python-virtualenv
virtualenv -p /usr/bin/python3 py3env
source py3env/bin/activate
cd django_blog
pip install -r requirements/dev.txt
python3 manage.py syncdb
python3 manage.py migrate apps.blog
python3 manage.py runserver 0.0.0.0:8000

