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


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


p = [i for i in range(0, 24)]
random.shuffle(p)

r =[33,45,6,5,3,333,4]

edge = [i for i in range (0, 0)]

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 23) == get_min_max(p)) else "Fail")
print ("Pass" if ((3, 333) == get_min_max(r)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max(edge)) else "Fail")
#edge case where length of array is zero