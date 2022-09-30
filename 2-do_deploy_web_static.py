#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['44.192.52.135', '44.192.246.111']


def do_deploy(archive_path):
    """ Distribute file to server """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        file = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(file))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file, file))
        run('rm /tmp/{}.tgz'.format(file))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file, file))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(file))
        return True

    except Exception as e:
        print(e)
        return False
