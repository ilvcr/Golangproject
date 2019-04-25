#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: merge_pdf_file.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Wes Apr 25 19:56:12 2018
# Description: 根据关键字利用pdfminer获取文本，并返回该页面
#************************************************************************#


"""
目标：从pdf文件中抽取出含有关键字的页面，并将这些页面合并一个新的pdf文件
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
fp = open('mypdf.pdf', 'rb')
import re
import os
#来创建一个pdf文档分析器
parser = PDFParser(fp)
#创建一个PDF文档对象存储文档结构
document = PDFDocument(parser)
# 检查文件是否允许文本提取
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建一个PDF资源管理器对象来存储共赏资源
    rsrcmgr=PDFResourceManager()
    # 设定参数进行分析
    laparams=LAParams()
    # 创建一个PDF设备对象
    # device=PDFDevice(rsrcmgr)
    device=PDFPageAggregator(rsrcmgr,laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter=PDFPageInterpreter(rsrcmgr,device)
    # 处理每一页
    pageindex = []
    i = 0
    pattern = re.compile("collinear")
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # # 接受该页面的LTPage对象
        layout=device.get_result()   # return text image line curve
        for x in layout:
            if isinstance(x,LTText):
                if pattern.search(x.get_text()):
                    pageindex.append(i)
        i +=1
pdf_output = PdfFileWriter()
pdf_input = PdfFileReader(fp)
# 获取 pdf 共用多少页
for  j in pageindex:
    pdf_output.addPage(pdf_input.getPage(j))
final_path =os.path.join(r"C:\Users\tc\Desktop\final.pdf")
with open(final_path,"wb") as f:
    pdf_output.write(f)
fp.close()
