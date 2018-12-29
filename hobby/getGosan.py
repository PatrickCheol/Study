#-*- coding:utf-8 -*-

import httplib2
import os
import time
now = time.localtime()

ROOM_URI=['categoryUid1=ff8080813ed0c5c4013ed0d86aa50019&categoryUid1s=ff8080813ed0c5c4013ed0d86aa50019',
'categoryUid1=ff8080813ed0c5c4013ed0d3a342000e&categoryUid1s=ff8080813ed0c5c4013ed0d3a342000e,ff8080813ed0c5c4013ed0d42f60000f,ff8080813ed0c5c4013ed0d44a510010',
'categoryUid1=ff8080813ed0c5c4013ed0d506410012&categoryUid1s=ff8080813ed0c5c4013ed0d506410012,ff8080813ed0c5c4013ed0d5330f0013,ff8080813ed0c5c4013ed0d571db0014',
'categoryUid1=ff8080813ed0c5c4013ed0d4dde20011&categoryUid1s=ff8080813ed0c5c4013ed0d4dde20011',
'categoryUid1=ff8080813ed0c5c4013ed0d5c4ec0015&categoryUid1s=ff8080813ed0c5c4013ed0d5c4ec0015,ff8080813ed0c5c4013ed0d5e2750016,ff8080813ed0c5c4013ed0d5f9fe0017',
'categoryUid1=ff8080813ed0c5c4013ed0d851990018&categoryUid1s=ff8080813ed0c5c4013ed0d851990018',
'categoryUid1=9be51dd55a7dc0e4015a83ca1a9f048c&categoryUid1s=9be51dd55a7dc0e4015a83ca1a9f048c',
'categoryUid1=9be51dc24f86cbc7015089045a334784&categoryUid1s=9be51dc24f86cbc7015089045a334784']
print('고산 휴양림 비어있는 방 조회 스크립트 by 이상철')
while True:
	print("조회 원하는 달 ex)7월 => 7 (최대 현재 달 +1달 까지 조회 가능) : ")
	print("quit 입력 시 종료")
	MONTH = raw_input("입력 : ")
	if MONTH == 'quit':
		break
	print('')
	print('1. 캐라반')
	print('2. 숲속의 집')
	print('3. 산림 휴양관')
	print('4. 문화 휴양관')
	print('5. 웰빙 휴양관')
	print('6. 대회의실')
	print('7. 돔하우스')
	print('8. 정자')
	ROOM = raw_input("방 종류를 선택하세요 : ")

	URI = '/planweb/reservation/pension_dateTotalRoomList.9is?contentUid=ff8080813ec5f86e013ec9e52e3f0055&year=2017&month=%s&%s' % (MONTH,ROOM_URI[int(ROOM)-1])
	BODY=''
	HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Referer': 'https://rest.wanju.go.kr/index.9is?contentUid=ff8080813ec5f86e013ec9e4d3240053',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
	'Cookie': 'JSESSIONID=920D4023A81BED0FF5643C4C0F63D49F',
	'Host': 'rest.wanju.go.kr',
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}
	DAY = now.tm_mday
	METHOD = 'GET'
	URL = 'http://rest.wanju.go.kr%s' % URI

	http = httplib2.Http()
	MUG_FF_LIST=[]
	(STATUS,DATA) = http.request(URL,METHOD,headers = HEADERS,body=BODY)
	if STATUS.status == 200:
		TMP_S = DATA.find('<tbody>') + len('<tbody>')
		TMP_E = DATA.find('</tbody>',TMP_S)
		TBODY = DATA[TMP_S:TMP_E]

		JAVA_S = DATA.find('<script type="text/javascript">',50000) + len('<script type="text/javascript">')
		JAVA_END = DATA.find('function setMonth',JAVA_S)
		SCIRPT_INFO = DATA[JAVA_S:JAVA_END]


		MUG_ID_E=0
		while True:
			if SCIRPT_INFO.find('$("#',MUG_ID_E) < 0:
				break
			MUG_ID_S = SCIRPT_INFO.find('$("#',MUG_ID_E) + len('$("#')
			MUG_ID_E = SCIRPT_INFO.find('").html',MUG_ID_S)
			MUG_FF_LIST.append(SCIRPT_INFO[MUG_ID_S:MUG_ID_E])

		TMP_E = 0
		while True:
			if TBODY.find('<th>',TMP_E) < 0 :
				break
			TMP_S = TBODY.find('<th>',TMP_E) + len('<th>')
			TMP_E = TBODY.find('</th>',TMP_S)
			ROOM_NAME = TBODY[TMP_S:TMP_E].replace('<br/>',':')
			print('\n'+ROOM_NAME)

			TMP_TRE = TBODY.find('</tr>',TMP_E)
			ROOM_INFO = TBODY[TMP_E:TMP_TRE]
			FIND_TEXT = 'id="'

			TMP_EE = 0
			DAY_E = 0
			DAY_CNT = 0
			if ROOM_INFO.find('mug ff') > 0:
				continue
			while True:
				DAY_CNT+=1
				if ROOM_INFO.find(FIND_TEXT,DAY_E) < 0:
					break
				DAY_S = ROOM_INFO.find(FIND_TEXT,DAY_E) + len(FIND_TEXT)
				DAY_E = ROOM_INFO.find('" >',DAY_S)

				if (ROOM_INFO[DAY_S:DAY_E] not in MUG_FF_LIST):
					if DAY_CNT < DAY:
						continue
					else:
						print("@"+ROOM_INFO[DAY_S:DAY_E][-1:]+"일 " if DAY_CNT<10 else "@"+ROOM_INFO[DAY_S:DAY_E][-2:]+"일 ")