words = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 
        7: "pqrs", 8: "tuv", 9: "wxyz"}


def compute_combinations(number: int):
	storageList = []
	first_input_string_counter = 0
	
	for num in  str(number):
		if len(str(number)) == 1:
			_letters = words[int(num)]
			storageList.append(_letters)
			return storageList

		if first_input_string_counter == 0:
			first_input_digit = words[int(num)]
			first_input_string_counter += 1
			continue

		other_input_digits = words[int(num)]
		for alphabet in first_input_digit:
			for letter in other_input_digits:
				storageList.append(alphabet + letter)
	return storageList


print(compute_combinations(23))