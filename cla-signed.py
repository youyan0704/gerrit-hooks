#!
# -*- coding: utf8 -*-
"""
__author__ = 'Yan' Started by '2019-08-07'

Description:
    Called whenever a user signs a contributor license agreement.

    cla-signed --submitter <submitter> --user-id <user_id> --cla-id <cla_id>

"""

from optparse import OptionParser


def main():
    usage = 'cla-signed --submitter <submitter> --user-id <user_id> --cla-id <cla_id>'
    des = 'cla-signed hooks'
    prog = '%prog'
    version = '1.0.0'
    p = OptionParser(usage=usage, description=des, prog=prog, version=version)
    p.add_option('--submitter', type=str, help='submitter')
    p.add_option('--user-id', type=str, help='user-id')
    p.add_option('--cla-id', type=str, help='cla-id')

    option, args = p.parse_args()

    print(option)


if __name__ == '__main__':
    main()
