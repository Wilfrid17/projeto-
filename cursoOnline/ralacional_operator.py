"""
HOW TO PROGRAM IN PYTHON -chapter
String formatting demostration
"""
print("Enter two integers, and i will tell you")
print("The relationships they satisfy.")

#read first string and convert to integer
NUMBER1 = input("please enter first integer: ")
NUMBER1 = int(NUMBER1)

#read second string and convert to integer
NUMBER2 = input("please enter second integer: ")
NUMBER2 = int(NUMBER2)

if NUMBER1 == NUMBER2:
    print("%d is equal to %d " %(NUMBER1, NUMBER2))

if NUMBER1 != NUMBER2:
    print("%d is not equal to %d" %(NUMBER1, NUMBER2))

if NUMBER1 < NUMBER2:
    print("%d is less than %d" %(NUMBER1, NUMBER2))

if NUMBER1 > NUMBER2:
    print("%d is greater than %d" %(NUMBER1, NUMBER2))

if NUMBER1 <= NUMBER2:
    print("%d is less than or equalo %d" %(NUMBER1, NUMBER2))

if NUMBER1 >= NUMBER2:
    print("%d is greater than or equal to %d" %(NUMBER1, NUMBER2))
