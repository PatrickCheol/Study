from urllib import parse
import requests
import openpyxl
import json

CVS_LOGIN_INFO = {
	'memberId':'', #CVS 로그인 아이디
	'memberKey':'' #CVS 로그인 패스워드
}

CVS_POST_INFO = {
	'csrfPreventionSalt':'',
	'goods_kind':'01',
	'exemption_agree':'Y',
	'goods_price':'2',
	'reserved_comments':'', #예약 이름
	'addrType':'01',
	'real_sender_name':'', #보내는사람 이름
	'real_sender_telno1':'010', #보내는 사람 번호1
	'real_sender_telno2':'', #보내는 사람 번호2
	'real_sender_telno3':'', #보내는 사람 번호3
	'real_sender_post_no':'', #보내는 사람 우편번호
	'real_sender_addr':'', #보내는 사람 주소
	'real_sender_detaddr':'', #보내는 사람 상세주소
	'receiver_name':'', #받는사람 이름
	'receiver_telno1':'', #받는사람 핸드폰 번호
	'receiver_telno2':'', #받는사람 핸드폰 번호
	'receiver_telno3':'', #받는사람 핸드폰 번호
	'add_receiver_telno1':'', 
	'add_receiver_telno2':'',
	'add_receiver_telno3':'',
	'receiver_postno':'', #받는사람 우편번호
	'receiver_addr':'', #받는사람 주소
	'receiver_detail_addr':'', #받는사람 주소 상세
	'special_contents':'',
	'pay_flag':'1'
}

ADDR_GET = {
	'confmKey':'', #API 사용 키
	'currentPage':'1',
	'countPerPage':'10',
	'resultType':'json',
	'keyword':''
}

def Reserve_POST():

	URL="http://www.juso.go.kr/addrlink/addrLinkApi.do?"

	excel_document = openpyxl.load_workbook('sample.xlsx')
	sheet = excel_document['Sheet1']
	i=2

	
	while sheet['A'+str(i)].value!=None:
		name=sheet['A'+str(i)].value
		s_Addr=sheet['B'+str(i)].value
		d_Addr=sheet['C'+str(i)].value
		phone=sheet['D'+str(i)].value

		ADDR_GET['keyword']=s_Addr

		with requests.Session() as s:
			addr_req=s.get('http://www.juso.go.kr/addrlink/addrLinkApi.do?',data=ADDR_GET)
			html_Json=addr_req.json()
			print(html_Json)


			if html_Json["results"]["common"]["errorCode"]!="0":
				print("Error")
			else:
				CVS_POST_INFO['reserved_comments']=name
				CVS_POST_INFO['receiver_name']=name
				CVS_POST_INFO['receiver_telno1']=phone.split('-')[0]
				CVS_POST_INFO['receiver_telno2']=phone.split('-')[1]
				CVS_POST_INFO['receiver_telno3']=phone.split('-')[2]
				CVS_POST_INFO['receiver_postno']=html_Json["results"]["juso"][0]["zipNo"]
				CVS_POST_INFO['receiver_addr']=html_Json["results"]["juso"][0]["roadAddr"]
				CVS_POST_INFO['receiver_detail_addr']=d_Addr

		login_req=s.post('https://www.cvsnet.co.kr/member/login/setLogin.do',data=CVS_LOGIN_INFO)
		#로그인 세션 가져옴

		post_req=s.post('https://www.cvsnet.co.kr/reservation-inquiry/domestic/all-insert.do',data=CVS_POST_INFO)
		i+=1
	


if __name__ == '__main__':
	Reserve_POST()
