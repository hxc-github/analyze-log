# -*- coding: utf-8 -*-


log_dict_html = {
    'content_length': '38093',
    'code': '200',
    'protocol': 'HTTP/1.1',
    'url': '/coding/miniproject/material.html',
    'ip': '200.200.76.130',
    'datetime': '16/Feb/2019:11:27:20 +0800',
    'method': 'GET'
}

log_dict_css = {
    'content_length': '63',
    'code': '200',
    'protocol': 'HTTP/1.1',
    'url': '/coding/gitbook/gitbook-plugin-disqus/plugin.css',
    'ip': '200.200.76.130',
    'datetime': '16/Feb/2019:11:27:20 +0800',
    'method': 'GET'
}

log_dict_js = {
    'content_length': '8305',
    'code': '200',
    'protocol': 'HTTP/1.1',
    'url': '/coding/gitbook/gitbook-plugin-search-plus/search.js',
    'ip': '200.200.76.130',
    'datetime': '16/Feb/2019:11:27:20 +0800',
    'method': 'GET'
}

article_report_dict = {
    '/coding/miniproject/material.html': {
        'ip_set': ['200.200.76.130', '200.200.76.132'],
        'ip_count': 1,
        'access_count': 2,
        'title': ''
    }
}

title = r'<title>test analyze log</title>'

log_list = [
    {
        'content_length': '38093',
        'code': '200',
        'protocol': 'HTTP/1.1',
        'url': '/coding/miniproject/material.html',
        'ip': '200.200.76.130',
        'datetime': '16/Feb/2019:11:27:20 +0800',
        'method': 'GET'
    },
    {
        'content_length': '1095',
        'code': '200',
        'protocol': 'HTTP/1.1',
        'url': '/coding/gitbook/gitbook-plugin-search-plus/search.css',
        'ip': '200.200.76.130',
        'datetime': '16/Feb/2019:11:27:20 +0800',
        'method': 'GET'
    },
    {
        'content_length': '63',
        'code': '200',
        'protocol': 'HTTP/1.1',
        'url': '/coding/gitbook/gitbook-plugin-disqus/plugin.css',
        'ip': '200.200.76.130',
        'datetime': '16/Feb/2019:11:27:20 +0800',
        'method': 'GET'
     },
    {
        'content_length': '3290',
        'code': '200', 'protocol': 'HTTP/1.1',
        'url': '/coding/gitbook/gitbook-plugin-prism/prism-base16-ateliersulphurpool.light.css',  # noqa: E501
        'ip': '200.200.76.130',
        'datetime': '16/Feb/2019:11:27:20 +0800',
        'method': 'GET'
    },
    {
        'content_length': '113099',
        'code': '200',
        'protocol': 'HTTP/1.1',
        'url': '/coding/gitbook/theme.js',
        'ip': '200.200.76.130',
        'datetime': '16/Feb/2019:11:27:20 +0800',
        'method': 'GET'
    },
    {
        'content_length': '1221',
        'code': '404',
        'protocol': 'HTTP/1.1',
        'url': '/designing/tools/image/gitbook/images/favicon.ico',
        'ip': '177.1.81.42',
        'datetime': '16/Feb/2019:11:28:49 +0800',
        'method': 'GET'
    },
    {
        'content_length': '156676',
        'code': '200',
        'protocol': 'HTTP/1.1',
        'url': '/designing/tools/image/UML_classes.docx',
        'ip': '177.1.81.42',
        'datetime': '16/Feb/2019:11:28:54 +0800',
        'method': 'GET'
    }
]

article_report_no_ip_num = {
    '/coding/miniproject/material.html': {
        'ip_set': set(['200.200.76.130']),
        'ip_count': 1,
        'access_count': 2,
        'title': ''
    },
    '/designing/tools/image/UML_classes.docx': {
        'ip_set': set(['177.1.81.42']),
        'ip_count': 1,
        'access_count': 1,
        'title': ''
    }
}

ip_report = {
    '177.1.81.42': {
        'access_count': 3,
        'article_count': 1
    },
    '200.200.76.130': {
        'access_count': 37,
        'article_count': 2
    }
}

complete_report = {
    '177.1.81.42/designing/tools/image/UML_classes.docx': {
        'url': '/designing/tools/image/UML_classes.docx',
        'ip': '177.1.81.42',
        'access_count': 1
    },
    '177.1.81.42/designing/tools/image/favicon.ico': {
        'url': '/designing/tools/image/favicon.ico',
        'ip': '177.1.81.42',
        'access_count': 1
    },
    '200.200.76.130/coding/gitbook/theme.js': {
        'url': '/coding/gitbook/theme.js',
        'ip': '200.200.76.130',
        'access_count': 1
    },
    '200.200.76.130/coding/gitbook/gitbook-plugin-prism/prism-base16-ateliersulphurpool.light.css':{  # noqa: E501
        'url': '/coding/gitbook/gitbook-plugin-prism/prism-base16-ateliersulphurpool.light.css',  # noqa: E501
        'ip': '200.200.76.130',
        'access_count': 1
    },
    '200.200.76.130/coding/gitbook/gitbook-plugin-disqus/plugin.css':{
        'url': '/coding/gitbook/gitbook-plugin-disqus/plugin.css',
        'ip': '200.200.76.130',
        'access_count': 1
    },
    '200.200.76.130/coding/gitbook/gitbook-plugin-search-plus/search.css':{
        'url': '/coding/gitbook/gitbook-plugin-search-plus/search.css',
        'ip': '200.200.76.130',
        'access_count': 1
    },
    '200.200.76.130/coding/miniproject/material.html':{
        'url': '/coding/miniproject/material.html',
        'ip': '200.200.76.130',
        'access_count': 2
    }
}
