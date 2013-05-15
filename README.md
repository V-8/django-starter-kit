<h3>Toolkit for django project creation and deployment</h3>

<b>Stack: Nginx + Gunicorn(with Supervisor) + Django + PostgreSQL</b><br/>

<b>django.sh</b> -- Script for creating django project(development/production/git repository).<br/>
<b>fabricfile.py</b> -- Automation tasks are all defined in this fabric file.<br/>
<b>requirements.txt</b> -- Install list for pip.<br/>
<b>gunicorn.sh</b> -- Script for starting gunicorn.<br/>
<b>supervisord.conf</b> -- Configuration for supervisord, which actutally start/stop gunicorn.
