from setuptools import setup, find_packages

setup(
    name='shadon_Test',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='',
    author='php-include',
    author_email='haikun2012@qq.com',
    description='shadon 框架专用自动化测试项目',
    install_requires=['requests', 'selenium','beautifulsoup4','lxml']
)
