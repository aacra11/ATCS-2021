"""
Ms. Namasivayam
ATCS 2021-2022
Recursion Tester

Runs unit tests to determine if the functions of recursion.py are accurate.
"""

from recursion import *


# Test factorial function
def testRecursion(func, input, expected, testName="Test"):
    result = func(input)
    if result == expected:
        print(testName + " passed")
    else:
        print(testName + " failed")
        print("Expected: ", expected)
        print("But got: ", result, '\n')


if __name__ == '__main__':
    # Test Factorial
    print('\n--------Test Factorial--------')
    testRecursion(factorial, 6, 720, "Test Factorial 1")
    testRecursion(factorial, 10, 3628800, "Test Factorial 2")
    testRecursion(factorial, 0, 1, "Test Factorial 3")
    testRecursion(factorial, 1, 1, "Test Factorial 4")

    # Test Countdown
    print('\n--------Test Countdown--------')
    testRecursion(countdown, 10, '10 9 8 7 6 5 4 3 2 1 Blastoff!', "Test Countdown 1")
    testRecursion(countdown, 0, 'Blastoff!', "Test Countdown 2")
    testRecursion(countdown, 1, '1 Blastoff!', "Test Countdown 3")

    # Test Reverse
    print('\n--------Test Reverse--------')
    testRecursion(reverse, 'Karel', 'leraK', "Test Reverse 1")
    testRecursion(reverse, 'a', 'a', "Test Reverse 2")
    testRecursion(reverse, 'bab', 'bab', "Test Reverse 3")

    # Test Bacteria
    print('\n--------Test Bacteria--------')
    testRecursion(numBacteriaAlive, 0, 10, "Test Bacteria 1")
    testRecursion(numBacteriaAlive, 1, 30, "Test Bacteria 2")
    testRecursion(numBacteriaAlive, 10, 590490, "Test Bacteria 3")
