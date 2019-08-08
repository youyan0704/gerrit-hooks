#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a patchset is created (this includes new changes).

    patchset-created --change <change id> --kind <change kind> --change-url <change url>
    --change-owner <change owner> --change-owner-username <username>
    --project <project name> --branch <branch> --topic <topic>
    --uploader <uploader> --uploader-username <username>
    --commit <sha1> --patchset <patchset id>

    The --kind parameter represents the kind of change uploaded.
    See documentation of patchSet for details.
"""

from optparse import OptionParser


def main():
    usage = 'patchset-created --change <change id> --kind <change kind> --change-url <change url> ' \
            '--change-owner <change owner> --change-owner-username <username> ' \
            '--project <project name> --branch <branch> --topic <topic> ' \
            '--uploader <uploader> --uploader-username <username> ' \
            '--commit <sha1> --patchset <patchset id> '
    des = 'patchset-created hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--kind', type=str, help='kind')
    p.add_option('--change-url', type=str, help='change-url')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--change-owner-username', type=str, help='change-owner-username')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--topic', type=str, help='topic')
    p.add_option('--uploader', type=str, help='uploader')
    p.add_option('--uploader-username', type=str, help='uploader-username')
    p.add_option('--commit', type=str, help='commit')
    p.add_option('--patchset', type=str, help='patchset')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
