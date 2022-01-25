"""
Alexandre Acra
ATCS 2021-2022
Recursion Assignment

Python program with various recursive functions
"""

# A factorial is a number multiplied by each positive integer smaller
# than itself. For example, 4 factorial (written as 4!) is 4 * 3 * 2 * 1
def factorial(num):
    # base case
    if (num==1):
        return 1
    # recursive case
    return(num*factorial(num-1))

# define countdown function:
def countdown(num):
    st=""
    # base case
    if (num==0):
        st = st+("Blast Off!")
        return st
    # recursive case
    st = st + str(num)
    return (st + (countdown(num-1)))

#define the reverse function
def reverse(word):
    # base case
    if(len(word) == 1):
        return word
    # recursive case
    return reverse(word[1:]) + word[0]

# define the bacteria culture function
def numBacteriaAlive(hours):
    # base case
    if(hours==0):
        return 10
    # recursive case
    return numBacteriaAlive(hours-1)*3

if __name__ == '__main__':
    # Test your functions here or run test_recursion.py
    print(factorial(6))
    print(countdown(10))
    print(reverse("Karel"))
    print(numBacteriaAlive(10))
