#!
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a ref has been updated.

    ref-updated --oldrev <old rev> --newrev <new rev> --refname <ref name>
    --project <project name> --submitter <submitter> --submitter-username <username>

"""

from optparse import OptionParser


def main():
    usage = 'ref-updated --oldrev <old rev> --newrev <new rev> --refname <ref name> ' \
            '--project <project name> --submitter <submitter> --submitter-username <username>'
    des = 'ref-updated hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--project', type=str, help='project')
    p.add_option('--refname', type=str, help='refname')
    p.add_option('--submitter', type=str, help='submitter')
    p.add_option('--submitter-username', type=str, help='submitter-username')
    p.add_option('--oldrev', type=str, help='oldrev')
    p.add_option('--newrev', type=str, help='newrev')
    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
