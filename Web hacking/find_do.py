import httplib2
import sys

http = httplib2.Http()

if len(sys.argv) != 3:
    print('python SEARCH_URL.py [TARGET_HOST] [TARGET_URL]')
    sys.exit()
    
TARGET_HOST = sys.argv[1]
TARGET_URL = sys.argv[2]

TMP = TARGET_URL.split('/')
HOST = TMP[2]

GET_LIST = []

HEADER = {'Host': HOST,
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Referer': 'http://www.beautynet.co.kr/',
          'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
          'Cookie': 'WMONID=-0uE1cAfxBT; wcs_bt=d93416ae1c7eec:1496543853; _ga=GA1.3.999384330.1496543725; _gid=GA1.3.834850462.1496543725; JSESSIONID=4M8UcmgJGAVmEaEx6mQAyxP6.server_44',
          'Connection': 'close'}


response, content = http.request(TARGET_URL, 'GET', headers=HEADER)
if response.status == 200:
    TMP_E = 0
    CHECK_CONTENT = content.replace('"', '\'')
    
    while True:
        if CHECK_CONTENT.find('\'', TMP_E) < 0:
            break

        TMP_S = CHECK_CONTENT.find('\'', TMP_E) + len('\'')
        TMP_E = CHECK_CONTENT.find('\'', TMP_S)

        CHECK_TEXT = CHECK_CONTENT[TMP_S:TMP_E]
        if '.do' in CHECK_TEXT and TARGET_HOST in CHECK_TEXT:
            if CHECK_TEXT not in GET_LIST:
                GET_LIST.append(CHECK_TEXT)

for URL in GET_LIST:
    print(URL)
