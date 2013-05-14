#!/bin/bash

################################################
# Program: 
# 启动gunicorn
# History: 
# 2013/05/14 zhouwei.evergreen@gmail.com First release 
################################################
 
set -e
LOGFILE=/var/log/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=10
# user/group to run as
USER=root
GROUP=root
ADDRESS=127.0.0.1:8000
SETTINGS=myproject.settings_production
WORKDIR=/var/www/production/env_mytest/myproject
cd $WORKDIR
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS \
    --settings=$SETTINGS \
    --pythonpath=$WORKDIR \
    --bind=$ADDRESS \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE