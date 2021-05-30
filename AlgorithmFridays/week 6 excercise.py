words = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 
        7: "pqrs", 8: "tuv", 9: "wxyz"}


def compute_combinations(number: int):
	storageList = []
	counter = 0
	
	for nums in  str(number):
		if len(str(number)) == 1:
			m = words[int(nums)]
			storageList.append(m)
			return storageList

		if counter == 0:
			v = words[int(nums)]
			counter += 1
			continue

		m = words[int(nums)]
		for l in v:
			for i in m:
				storageList.append(l+i)
	return storageList
		
print(compute_combinations(234))