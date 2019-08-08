#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a change’s topic is changed from the Web UI or via the REST API.

    topic-changed --change <change id> --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --changer <changer> --changer-username <username>
    --old-topic <old topic> --new-topic <new topic>

"""

from optparse import OptionParser


def main():
    usage = 'topic-changed --change <change id> --change-owner <change owner> --change-owner-username <username> ' \
            '--project <project name> --branch <branch> --changer <changer> --changer-username <username> ' \
            '--old-topic <old topic> --new-topic <new topic>'
    des = 'topic-changed hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--change-owner-username', type=str, help='change-owner-username')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--changer', type=str, help='changer')
    p.add_option('--changer-username', type=str, help='changer-username')
    p.add_option('--old-topic', type=str, help='old-topic')
    p.add_option('--new-topic', type=str, help='new-topic')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
