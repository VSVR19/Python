num = "-327 word words wordsss"

num = num.strip()
num_list = num.split(" ")

if(num_list[0].strip("-").isdigit()):
	
	if(int(num_list[0].strip(" ")) > 32767):		
		print("Exceeding Int +ve")

	elif(int(num_list[0].strip(" ")) < -32767):		
		print("Exceeding Int -ve")

	else:
		print(num_list[0])

else:
	print(0)