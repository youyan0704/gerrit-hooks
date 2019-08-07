#!
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a project has been created.

    project-created --project <project name> --head <head name>
"""

from optparse import OptionParser


def main():
    usage = 'project-created --project <project name> --head <head name>'
    des = 'project-created hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--project', type=str, help='project')
    p.add_option('--head', type=str, help='head')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
