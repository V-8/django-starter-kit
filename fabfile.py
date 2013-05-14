# -*- coding: UTF-8 -*-
from fabric.api import run, local
from fabric.state import env
from fabric.context_managers import lcd, cd
import os

#替换以下参数
#host_ip_address
#user_name
#project_name

#远程主机(git仓库+生产环境)
env.hosts = ['host_ip_address']  # 可配置多个远程主机
env.user = 'user_name'  # ssh账户

#本地开发环境配置
dev_env_dir = os.path.split(os.path.realpath(__file__))[0]
dev_dir = os.path.join(dev_env_dir, 'project_name')
install_file = os.path.join(dev_env_dir, 'requirements.txt')  # pip安装列表

#生产环境配置
deploy_env_dir = '/var/www/production/env_project_name'
deploy_dir = os.path.join(deploy_env_dir, 'project_name')


#测试用
def test():
    run('uname -a')


#初始化开发环境，首次执行
def setup_dev_env():
    with lcd(dev_env_dir):
        local('source bin/activate')
        with open(install_file) as f:
            for inst in f.readlines():
                local('pip install %s' % inst)


#初始化生产环境，首次执行
def setup_deploy_env():
    with cd(deploy_env_dir):
        run('source bin/activate')
        with open(install_file) as f:
            for inst in f.readlines():
                run('pip install %s' % inst)


#将开发代码push到远程git代码库
def push_to_repo():
    with lcd(dev_dir):
        local('git push origin master')


#从git代码库pull最新代码到生产环境
def pull_from_repo():
    with cd(deploy_dir):
        run('git pull origin master')


#重启guinicorn
def restart_appserver():
    with cd(deploy_env_dir):
        run('supervisorctl shutdown')
        run('supervisord -c supervisord.conf')


#自动部署
def deploy():
    push_to_repo()
    pull_from_repo()
    restart_appserver()

