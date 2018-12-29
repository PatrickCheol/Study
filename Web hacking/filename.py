import os

PATH = '/Users/patrick/Desktop/Python/Blind_Injection^information_schema.columns^concat(TABLE_SCHEMA,0x3a,TABLE_NAME,0x3a,COLUMN_NAME)^201707051328.txt'

FH = open(PATH,'r').read().split('\n')
for i in FH:
	if 'DATA_VALUE' in i:
		a = i.find('[')
		b = i.find(']')
		print(i[a+1:b])