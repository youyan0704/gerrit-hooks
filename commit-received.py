#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    This is called when a commit is received for review by Gerrit.
    It allows a push to be rejected before the review is created.

    If the hook exits with non-zero return code the push will be rejected.
    Any output from the hook will be returned to the user, regardless of the return code.

    commit-received --project <project name> --refname <refname> --uploader <uploader>
    --uploader-username <username> --oldrev <sha1> --newrev <sha1> --cmdref <refname>
"""

from optparse import OptionParser


def main():
    usage = 'commit-received --project <project name> --refname <refname> --uploader <uploader> ' \
            '--uploader-username <username> --oldrev <sha1> --newrev <sha1> --cmdref <refname>'
    des = 'commit-received hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--project', type=str, help='project')
    p.add_option('--refname', type=str, help='refname')
    p.add_option('--uploader', type=str, help='uploader')
    p.add_option('--uploader-username', type=str, help='uploader-username')
    p.add_option('--oldrev', type=str, help='oldrev')
    p.add_option('--newrev', type=str, help='newrev')
    p.add_option('--cmdref', type=str, help='cmdref')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
