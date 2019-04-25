#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: word2pdf.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 25 13:57:19 2019
# Description: 按文件夹批量转换word为pdf文件
#************************************************************************#

import os
from win32com.client import Dispatch, gencache, constants

def get_word_path(folder_path):
    '''
        定义一个获取指定文件夹路径下的word文档绝对路径的函数
    '''
    all_word_path = []
    file_list = os.listdir(folder_path)
    for file in file_list:
        if file.find('.docx') + 1:
            all_word_path.append(floder_path + '/' + file)
        else:
            pass

    return all_word_path

def create_pdf_path(folder_path, save_path):
    '''
        定义一个根据保存文件夹主路径生成的pdf文件绝对路径的函数
    '''
    pdf_path = []
    file_list = os.listdir(folder_path)
    for file in file_list:
        if file.find('.docx') + 1:
            pdf_path.append(save_path + '/' + file.split('.')[0] + '.pdf')
        else:
            pass
    return pdf_path

def word2pdf(src_path, dst_path):
    '''
        定义一个h将word转换为pdf的函数
    '''
    gencache.EnsureModule('{00020905-0000-0000-C0000-000000000046}',0, 8, 4)
    wd = Dispatch('Word.Application')
    for i in range(len(src_path)):
        doc = wd.Documents.Open(src_path[i], ReadOnly=1)
        doc.ExportAsFixedFormat(dst_path[i], constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    wd.Quit(constants.wdDoNotSaveChanges)


def main():
    word_folder_path = raw_input()
    pdf_floder_path = raw_input()

    word_file_path = get_word_path(word_folder_path)
    pdf_file_path = create_pdf_path(word_folder_path, pdf_floder_path)

    word2pdf(src_path=word_file_path, dst_path=pdf_file_path)

if __name__ == '__main__':
    main()




