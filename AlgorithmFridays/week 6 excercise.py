words = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 
        7: "pqrs", 8: "tuv", 9: "wxyz"}


def getletters(number: int):
	counter = 0
	for nums in  str(number):
		if counter == 0:
			v = words[int(nums)]
			print([v])
			counter += 1
			continue
		m = words[int(nums)]
		for l in v:
			for i in m:
				print([l+i])
		
	
    
getletters(234)