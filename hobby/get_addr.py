from bs4 import BeautifulSoup
from urllib import parse
import requests
import chardet
import openpyxl

URL="http://www.juso.go.kr/addrlink/addrLinkApi.do?"
U_confmKey="test"
U_currentPage="1"
U_countPerPage="10"

excel_document = openpyxl.load_workbook('sample.xlsx')
sheet = excel_document['Sheet1']
a=sheet['A1'].value
U_keyword=parse.quote(a)
U_resultType="json"
U_Search_URL=URL+"confmKey="+U_confmKey+"&"+"currentPage="+U_currentPage+"&"+"countPerPage="+U_countPerPage+"&"+"keyword="+U_keyword+"&"+"resultType="+U_resultType

print(U_Search_URL)

with requests.get(U_Search_URL) as response:
	html=response.text
	print(html)