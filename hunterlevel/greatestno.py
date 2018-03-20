
def createPalindrome(inp, b, isOdd):
    n = inp
    palin = inp
  
    # checks if number of digits is odd or even
    # if odd then neglect the last digit of input in
    # finding reverse as in case of odd number of
    # digits middle element occur once
    if (isOdd):
        n = n / b
  
    # Creates palindrome by just appending reverse
    # of number to itself
    while (n > 0):
        palin = palin * b + (n % b)
        n = n / b
    return palin
