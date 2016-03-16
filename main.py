#!/bin/env python
import re,sys
from scraper import ScraperHandler

class MainClass():

	def getIp(self):
		canReturn = False
		while not canReturn:
			fromIpStr = input("Enter the first IP: ")
			isIp = self.getIpFromStr(fromIpStr)
			if(isIp != False):
				self.fromIp = isIp
				ToIpStr = input("Enter the last IP: ")
				isIp = self.getIpFromStr(ToIpStr)
				if(isIp != False):
					self.toIp = isIp
					canReturn = True
				else:
					print("Wrong last IP")
			else:
				print("Wrong first IP")

	def getIpFromStr(self,ip):
		match = re.findall(r'([0-9]{1,3})',ip)
		if len(match) == 4:
			return match
		else:
			return False

	def __init__(self):
		self.getIp()
		scraper = ScraperHandler(self.fromIp,self.toIp)

if __name__ == '__main__':
	MainClass()