import PyPDF2


def from_pdf_read_txt():
	'''
		��pdf�ļ��м���ȡ�ı�
	'''
	with open('example.pdf', 'rb') as pdfFileObj:
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		print pdfReader.numPages
		pageObj = pdfReader.getPage(0)
		print pageObj.extractText()

import tabula

def from_pdf_read_excel():
	'''
		��pdf�ļ�����ȡ�������
	''' 
	df = tabula.read_pdf('example.pdf', multiple_tables=True)
	df.read()
	
	#���ض���ҳ���ȡ
	df = tabula.read_pdf('example.pdf', area=(126, 149, 212, 462), pages=1)
	df.read()

	#���ö�ȡ�����ΪJSON��ʽ
	df = tabula.read_pdf('example.pdf', output_format='json')
	df.read()

