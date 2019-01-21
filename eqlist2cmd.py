import re

with open('./fss_eq', 'r', encoding='UTF-8') as fin:
	for line in fin:
		if 'ˇ' in line:
			m = re.search('\\((.*)\\)', line)
			if m:
				print('get', m.group(1).lower())
				# print('get', m.group(1).split(' ')[-1])
