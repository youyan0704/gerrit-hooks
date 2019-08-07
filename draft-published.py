# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description：
    This is called whenever a draft change is published.

    draft-published --change <change id> --change-url <change url> --change-owner <change owner>
    --project <project name> --branch <branch> --topic <topic> --uploader <uploader> --commit <sha1> --patchset <patchset id>

"""

from optparse import OptionParser


def main():
    usage = 'draft-published --change <change id> --change-url <change url> --change-owner <change owner> ' \
            '--project <project name> --branch <branch> --topic <topic> --uploader <uploader> --commit <sha1> --patchset <patchset id>'
    des = 'draft-published hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--change', type=str, help='change')
    p.add_option('--change-url', type=str, help='change-url')
    p.add_option('--change-owner', type=str, help='change-owner')
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--topic', type=str, help='topic')
    p.add_option('--uploader', type=str, help='uploader')
    p.add_option('--commit', type=str, help='commit')
    p.add_option('--patchset', type=str, help='patchset')
    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()