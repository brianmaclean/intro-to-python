# complete this function so that it prints Hello, World
def printHelloWorld() :
    print("Hello, World")
    # your code here

# complete this function so that it prints whatever is provided in the parameter
def printParam(param) :
    print(param)
    # your code here

# complete this function so that it returns the sum of num1 and num2
def sumTwoNumbers(num1, num2) :
    return num1 + num2
    # your code here

# complete this function so that it returns the square of the num parameter
def findSquare(num) :
    return num * num
    # your code here

# complete this function so that it returns True if day is Wednesday
# otherwise return False
def dayIsWednesday(day) :
    if day == "Wednesday" :
        return True
    
    return False
    # your code here


myList = [ "mainsheet", "batton", "rudder", "foil", "block" ]

# complete this function so that it return "I got it" if item is in myList
# otherwise return "I have to get it"
def findInList(item) :
    for i in myList:
        if i == item :
            print("I got it")
        print("I have to get it")
    # your code here

# assuming every element in 'numList' is a number, complete this function so that it
# returns the total sum of the elements in the list
def complexSum(numList) :
    newSum = 0
    for number in numList:
        newSum += number
    return newSum
    # your code here


printHelloWorld()

printParam("sailing")

execute = sumTwoNumbers(5, 16)
print("sumTwoNumbers(5, 16) ", execute)

execute = findSquare(11)
print("findSquare(11) ", execute)

execute = dayIsWednesday("Tuesday")
print('dayIsWednesday("Tuesday") ', execute)

execute = dayIsWednesday("Wednesday")
print('dayIsWednesday("Wednesday") ', execute)

execute = findInList("rudder")
print('findInList("rudder") ', execute)

execute = findInList("quickdraw")
print('findInList("quickdraw") ', execute)

execute = complexSum([1, 3, 5, 7, 9])
print('complexSum([1, 3, 5, 7, 9]) ', execute)

execute = complexSum([2, 4, 6, 8, 10])
print('complexSum([2, 4, 6, 8, 10]) ', execute)