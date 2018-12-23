import math

class reverseNum():

	def __init__(self, num):
		self.num = num

	def revNum(self):
		revNum = 0
		neg = 0

		if(self.num < 0):			
			neg = 1

		num = abs(self.num)
		digits = int(math.log10(num)) + 1

		rem = 1
		i = 0
		j = 0

		while (rem > 0):
			quo = int((num / (10 ** (digits - 1))))	
			rem = int((num % (10 ** (digits - 1))))
			revNum = (quo * 1 * (10 ** i)) + revNum

			num = rem
			digits = digits - 1
			i = i + 1
		
		if(self.num == revNum):			
			return True
		else:
			return False

rn = reverseNum(324)
print(rn.revNum())