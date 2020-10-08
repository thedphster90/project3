
#Since an efficiency of log(n) is needed, I see no reason why a regular binary search cannot be used
#to solve this problem.

def rotated_array_search(input_list, number):
#Create two indexes and start in the middle.  Move outwards



    left_index = 0
    mid_index = (len(input_list)-1)//2
    right_index = len(input_list)-1



    if input_list[mid_index] == number:
        try:
            return mid_index
        except IndexError:
            print("indexerror")

    elif input_list[left_index] > number:
        return recursive_binary_search(input_list, number, mid_index+1, right_index)

    else:
         return recursive_binary_search(input_list, number, left_index, mid_index-1)





    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pass

def recursive_binary_search(input_list, number, left_index, right_index):

    if left_index > right_index:
        return -1


    mid_index = (right_index + left_index) // 2
    mid_ele = input_list[mid_index]

    if mid_ele == number:
        try:
            return mid_index
        except IndexError:
            print("indexerror")

    elif mid_ele > number:

        return recursive_binary_search(input_list, number, left_index, mid_index-1)

    else:
        return recursive_binary_search(input_list, number, mid_index+1, right_index)


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
#edge case in which the number is not a part of the array- should cause a pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#edge case where the array is not correct- both functions should return -1, which should cause a pass.
test_function([[0,0,0,0], 5])
