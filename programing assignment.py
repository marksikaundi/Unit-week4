# is_power function script

def is_divisible(a, b):
    return a % b == 0

def is_power(a, b):
    if a == 1:
        return True
    if b ==  1:
        return False
    if not is_divisible(a, b):
        return False
    return is_power(a/b, b)                        
    
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

# Discription 

# 1st base case:
# A number, a, is a power of b if both of them (a and b) are equal
# N.B. The only positive integer that is a power of "1" is "1" itself,

# 2nd base case:
# There is no any positive integer that is a power of "1", except the "1"
# itself, i.e., when b equals 1