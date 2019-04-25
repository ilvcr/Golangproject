#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: webpdf2text.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 26 22:32:55 2018
# Description: 
#************************************************************************#


from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdf_file)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    with open('webpdf.txt', 'a') as f:
        f.write(content)


if __name__ == '__main__':
    pdf_file = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
    readPDF(pdf_file)
