# �����ֲ�



# һ��������ʹ��
1��Linux��������analyze-log�ļ���

2�������й��߰�װ��

    python setup.py install

3��������ʹ��

    analyze-log --file-path --report-type [--filter-types] [--ip] [--func]

	--file-path: ��־�ļ�·����������־��
	--report-type: �������ͣ�Ŀǰֻ֧�����֣�
			'article-report'�����±���
			'ip-report'��IP����
			'complete-report'�� ��������
	--filter-types: ����ѡ�����˳�����־���ͣ�Ĭ���˳�css��js
	--ip������ѡ����http������Ҫ���ʵ�IP
	--func:����ѡ����ִ�й��ܣ�Ĭ�ϱ����ܣ�Ŀǰֻ֧�����֣�
			'report':���������
			'title':��ȡ���±��⹦��

4������ʹ��

�ٴ���ҳ��ȡ����
����ʹ��analyze-log --file-path apache.log --func title --ip 200.200.1.35��ȡ���±��⣬���������ݿ���
����ʹ��python main.py --file-path apache.log --func title --ip 200.200.1.35
�ڻ�ȡ������Ϣ
����������±���analyze-log --file-path apache.log --ip 200.200.1.35 --report-type article-report
����python main.py --file-path apache.log --ip 200.200.1.35 --report-type article-report
5������

����1��

    [root@hxc analyze-log]# analyze-log --file-path ./apache.log --report-type article-report --filter-type css js --ip isyk.xyz:8001
|URL|���±���|�����˴�|����IP��|
|----|-------|-------|--------|
|/coding/miniprj/material.html|����ͷ��|1|1|
|/designing/tools/image/UML_classes.docx||1|1|

����2��

	[root@hxc analyze-log]# analyze-log --file-path ./apache.log --report-type ip-report --filter-type css js
|IP|���ʴ���|����������|
|----|-------|--------|
|177.1.81.42|3|1|
|200.200.76.130|3|1|

����3��

	[root@hxc analyze-log]# analyze-log --file-path ./apache.log --report-type complete-report --filter-type css js
|IP|URL|���ʴ���|
|----|----|------|
|200.200.76.130|/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip|1|
|200.200.76.130|/coding/miniprj/material.html|1|
|200.200.76.130|/coding/gitbook/fonts/fontawesome/fontawesome-webfont.woff2?v=4.6.3|1|
|177.1.81.42|/designing/tools/image/favicon.ico|1|
|177.1.81.42|/designing/tools/image/gitbook/images/favicon.ico|1|
|177.1.81.42|/designing/tools/image/UML_classes.docx|1|

# ����ִ�е���

## 1��Linux������
	�����ذ�װrequests��mock, markdown_table, pytest, pytest-cov�⣬����pip install requests���װ
	�ڽ�analyze-log�ļ�����LinuxĿ¼��
	�۽���analyze-logĿ¼
	��ִ��pytest --cov ./ �����ִ�е�Ԫ���ԣ������ɸ�������Ϣ

# ����������

<img src="./cover.png" style="zoom:70%" />

