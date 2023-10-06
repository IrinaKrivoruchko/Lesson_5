import random
while True:
    try:
        NUM_SIZE = int(input("Enter size of list: "))
        break
    except:
        print("Enter only integer numbers please!")


numbers = []
for num in range(NUM_SIZE):
    numbers.append(random.randint(-100, 100))

print(numbers)
sum_negative = 0
sum_even = 0
sum_odd = 0
multiple = 1

#1
for num in numbers:
    if num < 0:
        sum_negative += num
    else:
        continue

print(f"Sum of negative numbers: {sum_negative}")

#2
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        continue

print(f"Sum of even numbers: {sum_even}")

#3
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
    else:
        continue

print(f"Sum of odd numbers: {sum_odd}")

#4
for i in range(len(numbers)):
    if i % 3 == 0:
        multiple *= numbers[i]
    else:
        continue

print(f"Product of elements with multiple indices of 3: {multiple}")