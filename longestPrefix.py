class longestPrefix():

	def __init__(self, wordList):
		self.wordList = wordList

	def findPrefix(self):
		try:			
			loopCounter = len(min(self.wordList, key = len))
			j = 0
			resultList = []

			for i in range(loopCounter):
				letters = [word[j] for word in self.wordList]
				j = j + 1

				setLetters = set(letters)
				listLetters = list(setLetters)
				stringLetter = "".join(listLetters)

				if(len(stringLetter) == 1):
					resultList.append(stringLetter)

			resultWord = "".join(resultList)

			if(len(resultWord) == 0):
				print("Oops!")
			else:
				print(resultWord)

		except(SyntaxError, IndexError, NameError):
			print('Exception!')

lp = longestPrefix(["Venkat", "Vijay", "Vikram"])
lp.findPrefix()