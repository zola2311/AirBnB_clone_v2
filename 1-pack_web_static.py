#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """

from fabric.api import local
import time


def do_pack():
    """ Generate .tgz file """
    timest = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timest))
        return ("versions/web_static_{:s}.tgz".format(timest))
    except Exception:
        return None
