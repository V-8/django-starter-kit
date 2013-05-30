# -*- coding: UTF-8 -*-
from fabric.api import run, local
from fabric.state import env
from fabric.context_managers import lcd, cd, prefix
import os

# 替换以下参数
# {host_ip_address}
# {user_name}
# {project_name}

# 远程主机(git仓库+生产环境)
env.hosts = ['{host_ip_address}']  # 可配置多个远程主机
env.user = '{user_name}'  # ssh账户

# 本地开发环境配置
dev_env_dir = os.path.split(os.path.realpath(__file__))[0]
dev_project_dir = os.path.join(dev_env_dir, '{project_name}')
install_file = os.path.join(dev_env_dir, 'requirements.txt')  # pip安装列表

# 生产环境配置
deploy_dir = '/var/www/production'
deploy_env_dir = os.path.join(deploy_dir, 'env_{project_name}')
deploy_project_dir = os.path.join(deploy_env_dir, '{project_name}')

# git服务器配置
repo_dir = '/opt/repos'
repo_project_dir = os.path.join(repo_dir, '{project_name}')

# 测试用
def test():
    run('uname -a')


# 将开发代码push到远程git代码库
def push_to_repo():
    with lcd(dev_project_dir):
        local('git push origin master')


# 从git代码库pull最新代码到生产环境
def pull_from_repo():
    with cd(deploy_project_dir):
        run('git pull origin master')


# Collect static files
def collect_static():
    with cd(deploy_project_dir):
        with prefix('source ../bin/activate'):
            run('python manage_production.py collectstatic')


# 重启guinicorn
def restart_appserver():
    with cd(deploy_env_dir):
        with prefix('source bin/activate'):
            run('supervisorctl shutdown')
            run('supervisord -c supervisord.conf')


# 自动部署，命令：fab deploy
def deploy():
    push_to_repo()
    pull_from_repo()
    restart_appserver()
    collect_static()


# 在git服务器上创建repository，并分别关联开发环境和生产环境
def setup():
    setup_dev_env()
    run('[ -d %s ] || mkdir %s' % (repo_dir, repo_dir))
    with cd(repo_dir):
        run('rm -rf {project_name} && git init --bare %s' % '{project_name}')
    with lcd(dev_project_dir):
        local('git init && git add . && git commit -m "initial commit"')
        local('git remote add origin %s@%s:%s' % ('{user_name}', '{host_ip_address}', repo_project_dir))
        local('git push origin master')
    run('[ -d %s ] || mkdir %s' % (deploy_dir, deploy_dir))
    with cd(deploy_dir):
        run('rm -rf env_{project_name} && mkdir env_{project_name}')
    with cd(deploy_env_dir):
        run('git clone %s' % repo_project_dir)
    setup_deploy_env()


# 初始化开发环境，首次执行
def setup_dev_env():
    with lcd(dev_env_dir):
        with prefix('source bin/activate'):
            with open(install_file) as f:
                for inst in f.readlines():
                    local('pip install %s' % inst)


# 初始化生产环境，首次执行
def setup_deploy_env():
    with cd(deploy_env_dir):
        run('virtualenv-2.7 .')
        with prefix('source bin/activate'):
            with open(install_file) as f:
                for inst in f.readlines():
                    run('pip install %s' % inst)
        run('wget https://raw.github.com/creativito/django-starter-kit/master/gunicorn.sh')
        run('wget https://raw.github.com/creativito/django-starter-kit/master/supervisord.conf')
        run('wget https://raw.github.com/creativito/django-starter-kit/master/nginx.conf')
        run("sed -i 's/{gunicorn_project_name}/{project_name}/g' gunicorn.sh && chmod 700 gunicorn.sh")
        run("sed -i 's/{gunicorn_project_name}/{project_name}/g' supervisord.conf")
        run("sed -i 's/{nginx_project_name}/{project_name}/g' nginx.conf")
        run("sed -i 's/{nginx_host_ip_address}/{host_ip_address}/g' nginx.conf")
