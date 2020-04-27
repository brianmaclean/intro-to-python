# write a function that takes a string 's' and prints it in reverse.
# Remember that a string is just an array of characters. Feel free to
# use additional arrays and variables to store any characters you might
# need.
def reverseStr(string) :
    # your code here
    s = string
    for i in s :
        s += i
    return s


# Given 'num' find if the value is prime or not.
# Remember to use '%' to find if something is divisible by something else.
def findIfPrime(num) :
    # your code here
  if num > 1 :
    for i in range(2, num//2) :
      if (num % i) == 0 :
        return False
    else :
      return True
  else :
    return False

# Given two numbers, find the greatest Common Divisor between those two
# numbers. If they are relatively prime, return -1.
def greatestCommonDivisor(num1, num2) :
    # your code here
    if (num2 == 0) :
        return num1
    else :
        return greatestCommonDivisor(num2, num1 % num2)
    


print("Reverse String: ", reverseStr('apples'))

print("Find If Prime (27): ", findIfPrime(27))

print("Find If Prime(19): ", findIfPrime(19))

print("Greatest Common Divisor (5, 10): ", greatestCommonDivisor(5, 10))

print("Greatest Common Divisor (7, 11): ", greatestCommonDivisor(7, 11))