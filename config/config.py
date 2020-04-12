# -*- coding:utf-8 -*-
__author__ = "leo"

import configparser
import os


def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.getcwd() + "/settings.conf"
    config.read(path)
    return config.get(section, key)
