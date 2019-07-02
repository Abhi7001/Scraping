from bs4 import BeautifulSoup
import urllib2
from xlwt import Workbook
import xlwt

def scrap():
	print('start')
	try:
		url="http://www.agriculture.gov.au/pests-diseases-weeds/plant#identify-pests-diseases"
		content = urllib2.urlopen(url).read()
		wb = Workbook()
		style = xlwt.easyxf('font: bold 1')
		sheet1=wb.add_sheet('scraping')
		sheet1.write(0,0,'S. No.',style)
		sheet1.write(0,1,'Disease name',style)
		sheet1.write(0,2,'Image link',style)
		sheet1.write(0,3,'Origin',style)
		sheet1.write(0,4,'See if you can identify the pest',style)
		sheet1.write(0,5,'Check what can legally come into Australia',style)
		sheet1.write(0,6,'Secure any suspect specimens',style)
		soup= BeautifulSoup(content, "lxml")
		res=soup.find("div",{"id":"collapsefaq"}).find("ul",{"class":"flex-container"}).find_all("li")
		count=0
		for li in res:
			if(li.find("a")['href'].startswith('/')):
				count=count+1
				disease_name=li.find("a").text
				img=li.find("a").find('img')['src']
				img_link="http://www.agriculture.gov.au"+img
				link=li.find("a")['href']
				url1="http://www.agriculture.gov.au"+link
				print(url1)
				content1=urllib2.urlopen(url1).read()
				soup1=BeautifulSoup(content1, "lxml")
				res1=soup1.find("div",{"class":"pest-header-content"})
				try:
					origin=res1.find_all("p")[1].find_all("strong")[1].next_sibling
				except Exception as e:
					if(e):
						continue
				div_class=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[0]['class']
			
				print('div_class',div_class[0])
				if(div_class == 'important-box-2'):
					n=1
					identify=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n]
					legal=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n+1]
					suspect=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n+2]
				else:
					n=0
					identify=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n]
					legal=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n+1]
					suspect=soup1.find("div",{"id":"ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"}).find("div",{"id":"collapsefaq"}).find_all("div")[n+2]
				sheet1.write(count,0,count)
				sheet1.write(count,1,disease_name)
				sheet1.write(count,2,img_link)
				sheet1.write(count,3,origin)
				sheet1.write(count,4,identify.get_text())
				sheet1.write(count,5,legal.get_text())
				sheet1.write(count,6,suspect.get_text())

				print("**********************************************")
#	print(res)
	except Exception as e:
		print(e)
	finally:
		wb.save('Data.xls')
	return "Done"

scrap()
