#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a reviewer is added to a change.

    reviewer-added --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --reviewer <reviewer> --reviewer-username <username>


"""

from optparse import OptionParser


def main():
    usage = 'reviewer-added --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username> ' \
            '--project <project name> --branch <branch> --reviewer <reviewer> --reviewer-username <username>'
    des = 'reviewer-added hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--change-url', type=str, help='change-url')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--change-owner-username', type=str, help='change-owner-username')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--reviewer', type=str, help='reviewer')
    p.add_option('--reviewer-username', type=str, help='reviewer-username')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
