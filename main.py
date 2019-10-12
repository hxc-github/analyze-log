# -*- coding: utf-8 -*-
import utils


def main():

    fil = utils.Filter()
    logs = fil.filter_log_by_type('test.txt')
    for log in logs:
        print log


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    main()
