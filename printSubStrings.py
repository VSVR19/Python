class subString():
	name = "cbbd"

	def __init__(self):
		pass

	def find_substrings(self):
		sub_list = []
		result_list = []

		for i in range(len(subString.name)):
			for j in range(len(subString.name)):
				sub_list.append	(subString.name[i : (j + 1)])

		for i in range(len(sub_list)):
			if(sub_list[i] == sub_list[i][::-1]):		
				result_list.append(sub_list[i])

		largest = max(result_list, key = len)
		return largest

subStr = subString()
print(subStr.find_substrings())