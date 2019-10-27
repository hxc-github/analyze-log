# -*- coding: utf-8 -*-
import logging

import log_parse
import log_filter
import report
import exc
from shell import init_args
from common import utils
from common import contants

logging.basicConfig(level=logging.INFO,
                    filename='analyze_log.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # noqa: E501

LOG = logging.getLogger(__name__)


def main():
    args = init_args()
    report_type = args.report_type
    ip = args.ip
    func = args.func

    logs = log_parse.parse_log_file(args.file_path)
    logs = log_filter.log_filter(logs, args.filter_types)

    if func == 'report':
        # 获取报表对象
        reports = report.get_report_obj(logs, report_type)
        # 获取相应类型报表内容
        report_dict = reports.gen_reports()
        # 将报表类型转换为列表
        display_attrs = utils.transform_to_list(report_dict, report_type)
        # 用markdown形式输出报表
        utils.display_by_markdown(contants.REPORT_NAME[report_type],
                                  contants.REPORT_ATTRS_DISPLAY[report_type],
                                  display_attrs
                                  )
    elif func == 'title':
        pass
    else:
        LOG.error('Don\'t support (%s) function')
        raise exc.FuncDontSupport('目前不支持（%s）功能' % func)


if __name__ == '__main__':
    main()

