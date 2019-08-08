#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a change has been merged.

    change-restored --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --topic <topic> --restorer <restorer> --restorer-username <username>
    --commit <sha1> --reason <reason>
"""

from optparse import OptionParser


def main():
    usage = 'change-restored --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username>' \
            '--project <project name> --branch <branch> --topic <topic> --restorer <restorer> --restorer-username <username>' \
            ' --commit <sha1> --reason <reason>'
    des = 'change-deleted hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--change-url', type=str, help='change-url')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--change-owner-username', type=str, help='change-owner-username')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--topic', type=str, help='topic')
    p.add_option('--restorer', type=str, help='restorer')
    p.add_option('--restorer-username', type=str, help='restorer-username')
    p.add_option('--commit', type=str, help='commit')
    p.add_option('--reason', type=str, help='reason')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
