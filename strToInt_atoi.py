class atoi():

	def __init__(self, num):
		self.num = num

	def strToAtoi(self):
		self.num = self.num.strip()
		num_list = self.num.split(" ")

		if(num_list[0].strip("-").isdigit()):
			if(int(num_list[0].strip(" ")) > 32767):		
				print("Exceeding Int +ve")

			elif(int(num_list[0].strip(" ")) < -32767):		
				print("Exceeding Int -ve")

			else:
				print(num_list[0])
		else:
			print(0)


at = atoi("-4199 word words wordsss")
at.strToAtoi()