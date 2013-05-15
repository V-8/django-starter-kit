<h3>Toolkit for django project creation and deployment</h3>

<b>Stack: Nginx + Gunicorn(with Supervisor) + Django + PostgreSQL</b><br/>

django.sh -- Script for creating django project(development/deployment/git repository).<br/>
fabricfile.py -- Automation tasks are all defined in this fabric file.<br/>
requirements.txt -- Install list for pip.<br/>
gunicorn.sh -- Script for starting gunicorn.<br/>
supervisord.conf -- Configuration for supervisord, which actutally start/stop gunicorn.
