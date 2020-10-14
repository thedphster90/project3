

#Used the Udacity lesson's "mergesort" function for this, which should be nlog(n) time complexity.
def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    sum_list1 = []
    sum_list2 = []
    #python can use a mergesort function has a worst case time complexity of nlog(n), fulfilling the requirements of the problem.
    input_list = mergesort(input_list)
    #input list length is odd
    if len(input_list)%2 == 1:
        odd = 0
        even = 0
        for i in range(0, len(input_list)-1):
            if odd == even:
                sum_list2.append(input_list[i])
                odd+=1
            else:
                sum_list1.append(input_list[i])
                even+=1
        #last appending due to the input list being odd
        sum_list1.append(input_list[len(input_list)-1])

        return num_maker(sum_list1, sum_list2)
    #If list number is not odd, its even
    else:
        odd = 0
        even = 0
        for i in range(0, len(input_list)):
            if odd == even:
                sum_list2.append(input_list[i])
                odd +=1
            else:
                sum_list1.append(input_list[i])
                even+=1
        return num_maker(sum_list1, sum_list2)

    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    pass

#This is a helper function that will turn two sorted lists from arrays into numbers
#call this function in the main rearrange digits funtion.
def num_maker(list1, list2):
    num1 = 0
    num2 = 0
    for i in range(0, len(list1)):
        if i > 0:
            num1 = num1 + (list1[i]*10**i)
        else:
            num1 = num1+ list1[0]
    for i in range(0, len(list2)):
        if i > 0:
            num2 = num2 + (list2[i]*10**i)
        else:
            num2 = num2+ list2[0]
    return num1, num2

    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case1)
test_function(test_case2)
#edge case
test_case3 = [[0,0,0,1], [10, 0]]
test_function(test_case3)
#edge case
#edge case that handles a single array input, works ok
test_case4 = [[0], [0, 0]]
test_function(test_case4)
