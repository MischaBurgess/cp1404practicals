"""Name writer task"""
print("*Name writer task*")
print()
output_file = 'name.txt'
out_file = open(output_file, 'w+')
name = input("What is your name?: ")
out_file.write(name)
out_file.close()

"""Name reader task"""
print("*Name reader task*")
print()
name_open = open("name.txt", 'r')
name_from_txt = name_open.readline()
print("Your name is: {}".format(name_from_txt))
print()
name_open.close()

"""Numbers task"""
print("*Number task*")
print()
try:
    numbers = open("numbers.txt", 'r')
    first_line = float(numbers.readline())
    second_line = float(numbers.readline())
    total = (first_line + second_line)
finally:
    print("The sum of the first two lines are: {:,.2f} ".format(total))
    print()
numbers.close()

"""Total for all numbers task"""
print("*Total for all numbers task*")
print()
number_file = "numbers.txt"
open_file = open(number_file, 'r')
total_sum = int(0)
for line in open_file:
    num = int(line)
    total_sum += num
print("The sum of all lines in the .txt is: {:,.2f}".format(total_sum))
print()
numbers.close()
