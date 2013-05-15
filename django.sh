#!/bin/bash

################################################
# Program: 
# django项目创建自动脚本(开发环境+git代码库+部署环境)
# History: 
# 2013/05/14 zhouwei.evergreen@gmail.com First release 
# Args:
# project_name=$1
# host_ip_address=$2
# user_name=$3
################################################

cd /Users/creativito/Documents/src/dev/
rm -rf env_$1
mkdir env_$1
cd env_$1
virtualenv-2.7 .
source bin/activate
pip install fabric
django-admin.py startproject $1

wget https://raw.github.com/creativito/django-starter-kit/bugfix/fabfile.py
wget https://raw.github.com/creativito/django-starter-kit/bugfix/requirements.txt

sed -i '' 's/{project_name}/'$1'/g' fabfile.py
sed -i '' 's/{host_ip_address}/'$2'/g' fabfile.py
sed -i '' 's/{user_name}/'$3'/g' fabfile.py

fab setup
fab restart_appserver

