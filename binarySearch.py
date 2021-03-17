#Nathan Li - Binary Search - 3/13/2021

numbers = [1,2,3,4,5,6,7,8,9,10]

#Iterative search
def binarySearch(list, target):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = (high + low)//2
        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid - 1
        else:
            return mid

print(binarySearch(numbers, 3))