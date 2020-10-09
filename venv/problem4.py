

#Note:  THis problem is identical to one of the lessons in the program, lesson2, num. 15.  I use
#the same code that I wrote for that problem for this problem.  Please let me know if this is a problem.
def sort_012(input_list):

    num_0 = 0
    num_2 = len(input_list) - 1
    main = 0

    while main <= num_2:
        if input_list[main] == 0:
            input_list[main] = input_list[num_0]
            input_list[num_0] = 0
            num_0 += 1
            main += 1
        elif input_list[main] == 2:
            input_list[main] = input_list[num_2]
            input_list[num_2] = 2
            num_2 -= 1
        else:
            main += 1
    return input_list

    pass

    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#edge case- This is already done so it should pass without having to sort, which the function should allow for
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#edge case- this has improper numbers so it shouldn't work
test_function([3,5,44,3])


