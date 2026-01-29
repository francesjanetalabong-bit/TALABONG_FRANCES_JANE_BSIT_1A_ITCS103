word = input("Please enter a word: ") # I'm asking the user to provide words

word_length = len(word) # len is used for measuring the letters inside the word

num_lst = [] # container where the number entered will be restored
print(f"Enter {word_length} numbers:") # f is used to concatinate 

for i in range(word_length): # for loop since limmeted only
	num = float(input(f"Number {i + 1 }" + ": "))  #float are usedd to bring decimal to the number entered by the user
	num_lst.append(num)

def  computing_average(num_list): # def was used to create my own function
	return sum(num_list) / len(num_list)

def compare_length_and_average(length, average): # using a conditional statement to determine the average based on the entered number.
	if length > average:
		return(f"The length of the '{word}' is greater than the average")
	elif length < average:
		return(f"The length of the '{word}'is less than the average")
	else:
		return(f"The length'{word}' is equal to the average")

average = computing_average(num_lst)
comparison_result = compare_length_and_average(word_length, average)
num_lst

print("\n-----The Result are:-----")
print("This is the list of the number entered:", num_lst)
print("List of the numbers entered:", num)
print("Length of the word entered:", word_length)
print("The Average of numbers entered:", average)
print(comparison_result)

