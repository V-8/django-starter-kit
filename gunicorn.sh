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
ADDRESS=0.0.0.0:8000
SETTINGS={gunicorn_project_name}.settings
WORKDIR=/var/www/production/env_{gunicorn_project_name}/{gunicorn_project_name}
cd $WORKDIR
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS \
    --settings=$SETTINGS \
    --pythonpath=$WORKDIR \
    --bind=$ADDRESS \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE