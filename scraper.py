import threading,urllib.request

class ScraperHandler():
	def main(self):
		while self.currentIp != self.toIp:
			if len(self.threads) <= 100:
				thread = Scraper(self.currentIp)
				self.threads.append(thread)
				thread.start()
				self.currentIp[3] = str(int(self.currentIp[3]) + 1)
				if self.currentIp[3] == "256":
					self.currentIp[3] = "0"
					self.currentIp[2] = str(int(self.currentIp[2]) + 1)
					if self.currentIp[2] == "256":
						self.currentIp[2] = "0"
						self.currentIp[1] = str(int(self.currentIp[1]) + 1)
			for t in self.threads:
				if t.finished:
					self.threads.remove(t)


	def __init__(self,fromIp,toIp):
		self.fromIp = fromIp
		self.toIp = toIp
		self.currentIp = fromIp
		self.threads = []
		self.main()


class Scraper(threading.Thread):
	def __init__(self,ip):
		threading.Thread.__init__(self)
		self.ip = ip
		self.finished = False

	def run(self):
		try:
			with urllib.request.urlopen("http://" + str.join(".",self.ip), timeout = 3) as response:
				html = response.read()
				if response.status == 200 or response.status == "200":
					print("I have found something at: http://" + str.join(".",self.ip) + "/")
		except:
			pass
		self.finished = True