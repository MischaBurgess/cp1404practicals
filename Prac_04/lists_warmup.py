"""List indexing warmup"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0]) # returns '3'
print(numbers[-1]) # returns '2'
print(numbers[3]) # returns '4'
print(numbers[:-1]) # returns '3, 1, 4, 1, 5, 9'
print(numbers[3:4]) # returns '1'
print(5 in numbers) # returns 'true'
print(7 in numbers) # returns 'false'
print("3" in numbers) # returns 'false'
print(numbers + [6, 5, 3]) # returns '3, 1, 4, 1, 5, 9, 6, 5, 3'
numbers[0] = "ten" # change the first element in the string to 'ten'
print(numbers)
numbers[-1] = 1 # change the last number to 1
print(numbers)
print(numbers[2:]) # get all elements except the first two
print(9 in numbers) # checks if 9 is an element in numbers