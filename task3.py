"""
===================   TASK 3   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def gcd(a, b):
    if a > b:
        result = b
    result = a

    if result == 1:
        return 1

    while result > 0:
        if a % result == 0 and b % result == 0:
            return result
        result -= 1

def main():
    a = 54
    b = 6
    res = gcd(a, b)
    print("Gcd is: ", res)

main()