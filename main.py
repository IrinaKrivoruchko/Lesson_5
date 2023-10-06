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
multiple_beetween_min_to_max = 1

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

#5
min_value = min(numbers)
max_value = max(numbers)

index_min_value = numbers.index(min_value)
index_max_value = numbers.index(max_value)

if index_min_value < index_max_value:
    new_numbers = numbers[index_min_value+1:index_max_value]
else:
    new_numbers = numbers[index_max_value+1:index_min_value]

for num in new_numbers:
    multiple_beetween_min_to_max *= num

print(f"Multiplication result of elements between the minimum and maximum element: {multiple_beetween_min_to_max}")