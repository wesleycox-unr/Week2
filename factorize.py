#% - Modulo

# Print the remainder for dividing each integer from 0 to 10 by 3

# 0 % 3 = 0
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1

# for
# range
# %

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divisor = 2

for number in range(0, 11):
    print(str(number) + " % " + str(divisor) + " = " + str(number%divisor))