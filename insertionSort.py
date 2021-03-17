#Nathan Li - Insertion Sort - 3/12/2021

numbers = [8,2,4,9,3,6]
for i in range(1, len(numbers)):
    key = i
    value = numbers[key]
    while value < numbers[key-1] and key > 0:
        numbers[key] = numbers[key-1]
        key -= 1
    numbers[key] = value

print(numbers)