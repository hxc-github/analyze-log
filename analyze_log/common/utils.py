# -*- coding: utf-8 -*-
import re
import markdown_table

import contants


def transform_to_list(report_dict, report_type):
    """
        将得到的字典型报表转化为列表
    :param report_dict: 字典型报表
    :type report_dict: dict
    :param report_type: 报表类型，文章报表，IP报表，完整报表
    :type report_type: str
    :return: 属性列表
    """
    display_attrs = list()
    for ip_url, info in report_dict.iteritems():
        attr_list = list()
        for attr in contants.REPORT_ATTRS[report_type]:
            attr_list.append(str(info[attr]))
        display_attrs.append(attr_list)
    return display_attrs


def display_by_markdown(table_name, attr_names, attrs):
    """
        输出为markdown形式
    :param table_name: 表格名称
    :type table_name: str
    :param attr_names: 需要显示的属性名称列表
    :type attr_names: list
    :param attrs: 属性列表[[...],[...]]
    :type attrs: list
    :return: None
    """
    table = markdown_table.Column(table_name)
    form = markdown_table.Table(attr_names, attrs)
    print table
    print form


def get_html_title(response):
    # 正则表达式匹配标题
    pat = r'<title>(?P<title>.*?)</title>'
    res = re.search(pat, str(response))
    if not res:
        return ''
    title = res.groupdict()['title']
    return title
