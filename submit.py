#!
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    This is called when a user attempts to submit a change.
    It allows the submit to be rejected.

    If the hook exits with non-zero return code the submit will be rejected
    and the output from the hook will be returned to the user.

    submit --project <project name> --branch <branch> --submitter <submitter> --patchset <patchset id> --commit <sha1>

"""

from optparse import OptionParser


def main():
    usage = 'submit --project <project name> --branch <branch> --submitter <submitter> --patchset <patchset id> --commit <sha1>'
    des = 'submit hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--project', type=str, help='project')
    p.add_option('--branch', type=str, help='branch')
    p.add_option('--submitter', type=str, help='submitter')
    p.add_option('--patchset', type=str, help='patchset')
    p.add_option('--commit', type=str, help='commit')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
