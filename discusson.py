#1) ("Debugging") lists three possibilities to consider if a function is not working.
    # First is something wrong with the arguments the function is getting, a precondition is violated.

    # Second, something wrong with the function, a postcondition is violated.

    # Third, something wrong with the return value or the way its being used.


#2) Define "precondition" and "postcondition" as part of your description. 

    #The "precondition" states the situation under which the function operates correctly, and the "postcondition" states what the function has accomplished when it terminates.


#3) Create your own example of each possibility in Python code. List the code for each example, along with sample output from trying to run it.
# codes below

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

print(factorial(7))