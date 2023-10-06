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

