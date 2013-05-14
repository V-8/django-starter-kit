<h3>方便django部署，自动创建项目并配置环境和git代码库</h3>

<b>Stack: Nginx+Gunicorn+Django+PostgreSQL</b><br/>

fabricfile.py -- 用fabric完成django项目模板和自动化部署<br/>
requirements.txt -- pip安装列表<br/>
django.sh -- 自动化创建django项目的脚本，调用fabric配置开发/生产环境和git代码库<br/>
gunicorn.sh -- 启动gunicorn服务
