# -*- coding: utf-8 -*-
import argparse
import sys
import logging

from report import display_report

logging.basicConfig(level=logging.INFO,
                    filename='analyze_log.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # noqa: E501


def init_args():
    parser = argparse.ArgumentParser(description='analyze apache log')

    # 必选参数
    parser.add_argument('--file-path',
                        type=str,
                        default=None,
                        required=True,
                        help='日志文件路径'
                        )
    parser.add_argument('--report-type',
                        type=str,
                        choices=['article-report', 'ip-report',
                                 'complete-report'],
                        default='complete-report',
                        required=True,
                        help='\r\n%(prog)s 参数选定报表类型, 默认: complete-report.\n' # noqa:E501
                             'article-report: 文章报表.\n'
                             'ip-report: IP报表.\n'
                             'complete-report： 完整报表.\n'
                        )
    # 可选参数
    parser.add_argument('--filter-types',
                        type=str,
                        nargs='*',
                        default=['css', 'js'],
                        help='过滤日志文件类型，默认过滤css和js文件.'
                        )
    parser.add_argument('--ip',
                        type=str,
                        default=None,
                        help='需要访问的ip')
    args, unparsed = parser.parse_known_args(sys.argv[1:])
    return args


def main():
    args = init_args()
    file_path = args.file_path
    report_type = args.report_type
    filter_types = args.filter_types
    ip = args.ip

    display_report(file_path=file_path, report_type=report_type,  # noqa: E501
                   filter_types=filter_types, ip=ip)
