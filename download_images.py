import urllib
import xlrd

def get_img():
	print('Start')
	try:
		loc=("Data.xls")
		wb = xlrd.open_workbook(loc)
		sheet = wb.sheet_by_index(0)
		print(sheet.nrows)
		for i in range(1,sheet.nrows):
			print(i)
			print(sheet.cell_value(i,2))
			urllib.urlretrieve(sheet.cell_value(i,2), str(i)+".jpg")
	except Exception as e:
		print(e)
	finally:
		print('Done')		

get_img()
