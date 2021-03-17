#Nathan Li - Merge Sort - 3/14/2021

numbers = [8,2,4,9,3,6,11,14,5,7]

def mergeSort(list):
    if len(list) > 1:
        left = list[:len(list)//2]
        right = list[len(list)//2:]
        mergeSort(left)
        mergeSort(right)
    
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        return(list)
    
print(mergeSort(numbers))