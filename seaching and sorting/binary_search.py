def binary_search(input_array, value):
    start=0
    end=len(input_array)
    while start<end:
        mid = (start+end)//2
        if input_array[mid]>value:
            end=mid
        elif input_array[mid]<value:
            start=mid+1
        else:
            return mid
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))