#!/bin/env python
import re,sys
from finder.scraper import ScraperHandler
from finder import utils

print ('Press CTRL+C to exit')
while True:
	print ('Enter the target ip range')
	fromIpString = input('From [192.168.0.1]:')
	toIpString = input('From [192.168.0.255]:')
	fromIp = utils.getIpFromStr((fromIpString, '192.168.0.1')[fromIpString == ''])
	toIp = utils.getIpFromStr((toIpString, '192.168.0.255')[toIpString == ''])
	scraper = ScraperHandler(fromIp, toIp, maxThreads=100)
