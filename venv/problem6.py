import random
#problem seems really easy.  Confirmed by looking at the mentor questions.
def get_min_max(ints):

    #edge case
    if len(ints) == 0:
        return print("Length of array is zero!!")

    min = ints[0]
    max = ints[0]

    for i in range(0, len(ints)):

        if ints[i] < min:
            min = ints[i]
        elif ints[i] > max:
            max = ints[i]
        else:
            pass

    return (min, max)



    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """


    pass


## Example Test Case of Ten Integers


test_list1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list1)


test_list2 = [i for i in range(0, 24)]
random.shuffle(test_list2)

test_list3 =[33,45,6,5,3,333,4]

test_list4 = [i for i in range(0, 100001)]  # a list containing 0 - 100000
random.shuffle(test_list4)

print ("Pass" if ((0, 9) == get_min_max(test_list1)) else "Fail")
print ("Pass" if ((0, 23) == get_min_max(test_list2)) else "Fail")
print ("Pass" if ((3, 333) == get_min_max(test_list3)) else "Fail")

print ("Pass" if ((0, 100000) == get_min_max(test_list4)) else "Fail")
#edge case where length of array is zero