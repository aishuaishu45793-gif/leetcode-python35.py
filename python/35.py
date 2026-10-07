# 105 Find the largest difference

numbers = [10, 5, 8, 20, 3]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

difference = largest - smallest

print("Largest difference:", difference)