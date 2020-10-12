

def sqrt(number):

    itnum = 0
    #This can be solved with a loop that gets a
    #first start with boundary conditions
    if number == 1:
        return 1
    elif number <= 0:
        return print("please only use positive numbers ;)")

    else:
        prev_num = number/2

        while True:

            new_num = (prev_num + number/prev_num)/2

            if abs(new_num - prev_num) < .00001: #this is the error that is accepted
                return int(prev_num)


            prev_num = new_num  #this will be the new test number for the next loop


"""
    Calculate the floored square root of a number
    
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
"""

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#This will fail because it will not return 0, but return a fail message
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

#all should print "Pass" except for the second one, which should print "fail"