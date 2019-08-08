#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description：
    This is called whenever a comment is added to a change.

    comment-added --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --topic <topic> --author <comment author> --author-username <username> --commit <commit>
    --comment <comment> [--<approval category id> <score> --<approval category id> <score> --<approval category id>-oldValue <score> ...]

"""

from optparse import OptionParser


def main():
    usage = 'comment-added --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username>' \
            '--project <project name> --branch <branch> --topic <topic> --author <comment author> --author-username <username> --commit <commit> ' \
            '--comment <comment> [--<approval category id> <score> --<approval category id> <score> ...]'
    des = 'comment-added hooks'
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
    p.add_option('--author', type=str, help='author')
    p.add_option('--author-username', type=str, help='author-username')
    p.add_option('--commit', type=str, help='commit')
    p.add_option('--comment', type=str, help='comment')
    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()