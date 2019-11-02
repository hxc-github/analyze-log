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
    },
]

article_report_no_ip_num = {
    '/coding/miniproject/material.html': {
        'url': '/coding/miniproject/material.html',
        'visitors': 2,
        'ip_set': set(['200.200.76.130']),
        'access_ip_num': 1,
        'title': ''
    },
    '/designing/tools/image/UML_classes.docx': {
        'url': '/designing/tools/image/UML_classes.docx',
        'visitors': 1,
        'ip_set': set(['177.1.81.42']),
        'access_ip_num': 1,
        'title': ''
    }
}

ip_num_report = {
    '/coding/miniproject/material.html': {
        'ip_set': ['200.200.76.130', '200.200.76.132'],
        'ip_count': 1,
        'access_ip_num': 2,
        'access_count': 2,
        'title': ''
    }
}

ip_report = {
    '177.1.81.42': {
        'ip': '177.1.81.42',
        'article_num': 1,
        'visitors': 2
    },
    '200.200.76.130': {
        'ip': '200.200.76.130',
        'article_num': 2,
        'visitors': 6
    }
}

ip_attrs = [['177.1.81.42', '2', '1'], ['200.200.76.130', '6', '2']]

title_report = {
    '/coding/miniproject/material.html': {
        'ip_set': ['200.200.76.130', '200.200.76.132'],
        'ip_count': 1,
        'access_ip_num': 2,
        'access_count': 2,
        'title': 'No title'
    }
}

complete_report = {
    '200.200.76.130/coding/gitbook/gitbook-plugin-disqus/plugin.css': {
        'url': '/coding/gitbook/gitbook-plugin-disqus/plugin.css',
        'ip': '200.200.76.130',
        'visitors': 1
    },
    '177.1.81.42/designing/tools/image/gitbook/images/favicon.ico': {
        'url': '/designing/tools/image/gitbook/images/favicon.ico',
        'ip': '177.1.81.42', 'visitors': 1},
    '200.200.76.130/coding/miniproject/material.html': {
        'url': '/coding/miniproject/material.html',
        'ip': '200.200.76.130',
        'visitors': 2
    },
    '200.200.76.130/coding/gitbook/gitbook-plugin-prism/prism-base16-ateliersulphurpool.light.css': {
        'url': '/coding/gitbook/gitbook-plugin-prism/prism-base16-ateliersulphurpool.light.css',
        'ip': '200.200.76.130',
        'visitors': 1
    },
    '200.200.76.130/coding/gitbook/gitbook-plugin-search-plus/search.css': {
        'url': '/coding/gitbook/gitbook-plugin-search-plus/search.css',
        'ip': '200.200.76.130',
        'visitors': 1
    },
    '200.200.76.130/coding/gitbook/theme.js': {
        'url': '/coding/gitbook/theme.js',
        'ip': '200.200.76.130',
        'visitors': 1
    },
    '177.1.81.42/designing/tools/image/UML_classes.docx': {
        'url': '/designing/tools/image/UML_classes.docx',
        'ip': '177.1.81.42',
        'visitors': 1
    }
}


class ReadTitle():

    def fetchone(self):
        return ('title test',)


class ReadTitleError():

    pass


log_no_url = {
    'content_length': '38093',
    'code': '200',
    'protocol': 'HTTP/1.1',
    'ip': '200.200.76.130',
    'datetime': '16/Feb/2019:11:27:20 +0800',
    'method': 'GET'
}
