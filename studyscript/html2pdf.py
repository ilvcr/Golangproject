#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: html2pdf.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 25 19:42:46 2019
# Description: 将网上的在线教程下载下来转换成PDF文件
#************************************************************************#


import requests
from beautifulsoup4 import BeautifulSoup
import pdfkit

def parse_url_to_html(url):
    '''
        使用soup.find_all函数找到正文标签,然后把正文部分
        的内容保存到a.html文件中
    '''
    response = requests(url)
    soup = BeautifulSoup(response.content, 'html.parse')
    body = soup.find_all(class_='x-wiki-content')[0]
    html = str(body)

    with open('a.html', 'wb') as f:
        f.writen(html)

def get_url_list(url):
    '''
        获取所有URL目录列表
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parse')
    menu_tag = soup.find_all(class_='uk_nav uk-nav-side')[1]
    urls = []

    for li in menu_tag.find_all('li'):
        url = 'exampleurl' + li.a.get('href')
        urls.append(url)
    return urls

def save_pdf(htmls):
    '''
        把所有的html文件转换为pdf文件
    '''
    options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'custom-header': [('Accept-Encoding', 'gzip')]
            }

    pdfkit.from_file(htmls, file_name, options=option)


