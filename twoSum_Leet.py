class twoSum():		

	def __init__(self):
		self.nums = nums
		self.target = target

	def calculate_twoSum(self):
		for i in range(len(nums)):
			for j in range(len(nums)):
				temp_target = nums[i] + nums[j]
				if(temp_target == target):
					return nums[i], nums[j]

nums = [2, 7, 11, 5]
target = 7	

twoSumObj = twoSum()
print(twoSumObj.calculate_twoSum())