import random
while True:
    try:
        NUM_SIZE = int(input("Enter size of list: "))
        if NUM_SIZE > 0:
            break
        if NUM_SIZE <= 0:
            print("You should to enter number more then 0")
    except ValueError:
        print("Enter only integer numbers please!")



numbers = []
for num in range(NUM_SIZE):
    numbers.append(random.randint(-100, 100))

print(numbers)

#First task
#1
# sum_negative = 0
# for num in numbers:
#     if num < 0:
#         sum_negative += num
#     else:
#         continue
#
# print(f"Sum of negative numbers: {sum_negative}")

#2
# sum_even = 0
# for num in numbers:
#     if num % 2 == 0:
#         sum_even += num
#     else:
#         continue
#
# print(f"Sum of even numbers: {sum_even}")

#3
# sum_odd = 0
# for num in numbers:
#     if num % 2 != 0:
#         sum_odd += num
#     else:
#         continue
#
# print(f"Sum of odd numbers: {sum_odd}")

#4
# multiple = 1
# for i in range(len(numbers)):
#     if i % 3 == 0:
#         multiple *= numbers[i]
#     else:
#         continue
#
# print(f"Product of elements with multiple indices of 3: {multiple}")

#5
# index_min_value = numbers.index(min(numbers))
# index_max_value = numbers.index(max(numbers))
#
# if index_min_value < index_max_value:
#     new_numbers = numbers[index_min_value+1:index_max_value]
# else:
#     new_numbers = numbers[index_max_value+1:index_min_value]
#
# multiple_beetween_min_to_max = 1
# if len(new_numbers) != 0:
#     for num in new_numbers:
#         multiple_beetween_min_to_max *= num
#     print(f"Multiplication result of elements between the minimum and maximum element: {multiple_beetween_min_to_max}")
# else:
#     print("The minimum and maximum values are next to each other")

#6
# index_first_positive_el = 0
# index_last_positive_el = 0
#
# for num in numbers:
#     if num > 0:
#         index_first_positive_el = numbers.index(num)
#         break
#
# for num in numbers:
#     if num > 0:
#         index_last_positive_el = numbers.index(num)
#     else:
#         continue
#
# sum_slice = 0
# new_num = numbers[index_first_positive_el + 1: index_last_positive_el]
# if len(new_num) != 0:
#     for i in new_num:
#         sum_slice += i
#     print(f"The sum of elements that are between the first and remaining positive elements: {sum_slice}")
# else:
#     print("The minimum and maximum values are next to each other")

#Second task
#1
# only_even = []
# for num in numbers:
#     if num % 2 == 0:
#         only_even.append(num)
#     else:
#         continue
# if len(only_even) != 0:
#     print(f"New list of integers containing only even numbers: {only_even}")
# else:
#     print("All numbers are odd")

#2
only_odd = []
for num in numbers:
    if num % 2 != 0:
        only_odd.append(num)
    else:
        continue
if len(only_odd) != 0:
    print(f"Create a list of integers containing only odd numbers: {only_odd}")
else:
    print("All numbers are even")