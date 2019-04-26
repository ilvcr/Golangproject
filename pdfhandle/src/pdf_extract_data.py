#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: pdf_extract_data.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr 24 15:57:19 2018
# Description: 按文件夹批量转换word为pdf文件
#************************************************************************#

import PyPDF2


def from_pdf_read_txt():
	'''
		从pdf文件中简单提取文本
	'''
	with open('example.pdf', 'rb') as pdfFileObj:
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		print pdfReader.numPages
		pageObj = pdfReader.getPage(0)
		print pageObj.extractText()

import tabula

def from_pdf_read_excel():
	'''
		从pdf文件中提取表格数据
	''' 
	df = tabula.read_pdf('example.pdf', multiple_tables=True)
	df.read()
	
	#从特定的页面读取
	df = tabula.read_pdf('example.pdf', area=(126, 149, 212, 462), pages=1)
	df.read()

	#设置读取的输出为JSON格式
	df = tabula.read_pdf('example.pdf', output_format='json')
	df.read()

