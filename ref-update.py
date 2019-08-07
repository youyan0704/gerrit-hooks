#!
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    This is called when a ref update request (direct push, non-fastforward update, or ref deletion) is received by Gerrit.
    It allows a request to be rejected before it is committed to the Gerrit repository.

    If the hook exits with non-zero return code the update will be rejected.
    Any output from the hook will be returned to the user, regardless of the return code.

  ref-update --project <project name> --refname <refname> --uploader <uploader>
    --uploader-username <username> --oldrev <sha1> --newrev <sha1>
"""

from optparse import OptionParser


def main():
    usage = 'ref-update --project <project name> --refname <refname> --uploader <uploader> --uploader-username <username> --oldrev <sha1> --newrev <sha1> '
    des = 'ref-update hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--project', type=str, help='project')
    p.add_option('--refname', type=str, help='refname')
    p.add_option('--uploader', type=str, help='uploader')
    p.add_option('--uploader-username', type=str, help='uploader-username')
    p.add_option('--oldrev', type=str, help='oldrev')
    p.add_option('--newrev', type=str, help='newrev')
    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
