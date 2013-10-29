#!/bin/bash

##############################################
# Python2.7.3 and related for CENTOS 6 X64
##############################################

### Python-2.7.3
yum install -y wget
yum -y groupinstall "Development tools"
yum -y install MySQL-python mysql-devel python-devel libevent-devel postgresql-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libjpeg libjpeg-devel
cd /root
wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2
tar xf Python-2.7.3.tar.bz2
cd Python-2.7.3
./configure --prefix=/usr/local
make && make altinstall

### distribute for Python-2.7.3
cd /root
wget http://pypi.python.org/packages/source/d/distribute/distribute-0.6.36.tar.gz --no-check-certificate
tar xf distribute-0.6.36.tar.gz
cd distribute-0.6.36
python2.7 setup.py install

### pyrad-2.0.tar.gz for Python-2.7.3
get pyrad-2.0.tar.gz(42.96.174.201ÓÐ)
tar xf pyrad-2.0.tar.gz
cd pyrad-2.0
python2.7 setup.py install

### pyOpenSSL (must be complied with openssl version)
#easy_install-2.7 http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-0.12.tar.gz

### pip for Python-2.7.3
cd /root
easy_install-2.7 pip

### virtualenv for Python-2.7.3
cd /root
pip-2.7 install virtualenv

### Set alias
cat >>/root/.bashrc<<EOF
alias python='python2.7'
EOF

### supervisor and fabric for process crontrol
pip install fabric
pip install supervisor

### Nginx
cd /root
wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
rpm -ivh nginx-release-centos-6-0.el6.ngx.noarch.rpm
yum install nginx

### Postfix
yum install -y postfix cyrus-sasl-plain

### Web projects directories
mkdir /var/www
mkdir /var/www/public
mkdir /var/www/production