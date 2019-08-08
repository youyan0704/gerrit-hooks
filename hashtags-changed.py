#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever hashtags are added to or removed from a change from the Web UI or via the REST API.

    hashtags-changed --change <change id>  --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --editor <editor> --editor-username <username>
    --added <hashtag> --removed <hashtag> --hashtag <hashtag>

    The --added parameter may be passed multiple times, once for each hashtag that was added to the change.

    The --removed parameter may be passed multiple times, once for each hashtag that was removed from the change.

    The --hashtag parameter may be passed multiple times, once for each hashtag remaining on the change
    after the add or remove operation has been performed.
"""

from optparse import OptionParser


def main():
    usage = 'hashtags-changed --change <change id>  --change-owner <change owner> --change-owner-username <username> ' \
            '--project <project name> --branch <branch> --editor <editor> --editor-username <username> ' \
            '--added <hashtag> --removed <hashtag> --hashtag <hashtag>'
    des = 'hashtags-changed hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--change-owner-username', type=str, help='change-owner-username')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--editor', type=str, help='editor')
    p.add_option('--editor-username', type=str, help='editor-username')
    p.add_option('--added', type=str, help='added')
    p.add_option('--removed', type=str, help='removed')
    p.add_option('--hashtag', type=str, help='hashtag')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
