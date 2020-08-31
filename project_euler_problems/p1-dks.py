#Sum of multiples of 3 or 5 below 1000

limit = 1000

numbers_list = []

for x in range(1,limit):
    if x % 3 == 0 or x % 5 == 0:
        numbers_list.append(x)
print(numbers_list)
print("Answer: ", sum(numbers_list))
