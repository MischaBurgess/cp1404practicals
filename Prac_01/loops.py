
for i in range(0, 110, 10):
    print(i, end=' ')
print("\r")

for j in range(20, 0, -1):
    print(j, end=' ')
print("\r")

no_of_stars = int(input("how many stars would you like?: "))
for k in range(0, no_of_stars):
    print("*", end='')
print("\r")

no_of_stars_pyramid = int(input("How many stars would you like for your pyramid?: "))
for K in range(0, no_of_stars_pyramid):
    for L in range(0, K + 1):
        print("* ", end="")
    print("\r")
