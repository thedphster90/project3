
#Since an efficiency of log(n) is needed, I see no reason why a regular binary search cannot be used
#to solve this problem.

def rotated_array_search(input_list, number):
#Create two indexes and start in the middle.  Move outwars

    mid_index = (len(input_list)-1)//2

    if input_list[mid_index] == number:
        return mid_index

    elif input_list[mid_index] > number:
        newlist = input_list[:mid_index-1]
        if newlist is None:
            return -1
        print(newlist)
        return rotated_array_search(newlist, number)

    else:
        newlist = input_list[mid_index+1:]
        if newlist is None:
            return -1
        print(newlist)
        return rotated_array_search(newlist, number)





    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])