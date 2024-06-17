# Find the largest num in the list

numbers = [1, 4, 67, 43, 28, 32]

# You can initialise the largest number to 1, or you can initialise to numbers index [0] => first element in the list ( it's better this way if list contains minus numbers,or zero)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
print("The largest number is",(largest))        