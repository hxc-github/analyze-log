# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='analyze-log',
    version='1.0',
    packages=['analyze_log'],
    entry_points={'console_scripts': ['analyze-log = analyze_log.shell:main']}
)
