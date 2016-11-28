import re

def getIpFromStr(ip):
	match = re.findall(r'([0-9]{1,3})',ip)
	if len(match) == 4:
		return match
	else:
		return False
