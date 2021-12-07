#PART 1
def hypotenuse(leg1,leg2): #our function has 2 arguments for first leg and second leg respectively
    return (leg1**2+leg2**2)**(1/2) #according to Pythagorean theorem, the hypotenuse is equal to the square root of the sum of the squares of the legs
                                   

  
print("Test number 1, triangle with legs 3 and 4, hypotenuse is:",hypotenuse(3,4))#prints the call for triangle with legs 3 and for
print("Expected 5")#expected result
print("Test number 1, triangle with legs 12 and 5, hypotenuse is:",hypotenuse(12,5))#same for 12 and 5
print("Expected 13")
print("Test number 1, triangle with legs 20 and 21, hypotenuse is:",hypotenuse(20,21))#20 and 29
print("Expected 29")

# out puts for the codes
    # Test number 1, triangle with legs 3 and 4, hypotenuse is: 5.0
    # Expected 5
    # Test number 1, triangle with legs 12 and 5, hypotenuse is: 13.0 
    # Expected 13
    # Test number 1, triangle with legs 20 and 21, hypotenuse is: 29.0
    # Expected 29

#PART 2
# Requirements:

# The task is to build the simple function to calculate the area of the circle inscribed 

# in a square with the certain side length

# Design:

# The solution to this task is simple: the area of the circle inscribed 

# in a square with the certain side length a is equal to pi*(a/2)^2. However pi is not a native python variable. We can find pi in math module that we need to import in advance.

# The desired function will return the area value to the user

# Implementation 1:
from math import pi
def circ_area_in_sq(a):
    a = float(a)
    return (pi*((a/2)**2))
        #Testing 1
print(circ_area_in_sq(0))
print(circ_area_in_sq(1))
print(circ_area_in_sq(2))

        # OUT PUTS
    # 0.0
    # 0.7853981633974483
    # 3.141592653589793

# Communication 2:

# It turned out that in some cases the function returns an exception. When the input is not a number the customer requires the function to return None

# Design 2:

# To handle this case an error handling has to be implemented.

# Implementation 2:
from math import pi
def circ_area_in_sq(a):
    try:
        a = float(a)
        return (pi*((a/2)**2))
    except ValueError:
        return None
        #Testing 2
print(circ_area_in_sq("not a number"))
print(circ_area_in_sq(3))
print(circ_area_in_sq(4))
None
        # outputs
    # 7.0685834705770345
    # 12.566370614359172

# Delivery 2:
# The code was delivered and deployed

# PART 3
# Describe your experience so far with peer assessment of Discussion Assignments.
# So far so good the experience is there, am learning quite number of things from my frends and they are always positive when it comes to give the feedback. 
# Ofcourse my feedback to them is always positive when it comes to peer them, there the chances of them feeling good are there.