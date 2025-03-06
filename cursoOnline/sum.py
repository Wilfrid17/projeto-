"""
HOW TO PROGRAM IN PYTHON -chater 3
 Sum two integers showing metadatas
"""

INTEGER1 =input("enter first integer: \n")
print("INTEGER1 : ", id(INTEGER1), type(INTEGER1), INTEGER1)
INTEGER1 = int(INTEGER1)
print("INTEGER1 : ", id(INTEGER1), type(INTEGER1), INTEGER1)

INTEGER2 = input("enter second integer: \n")
print("INTEGER2 :" , id(INTEGER2), type(INTEGER2), INTEGER2)
INTEGER2 = int(INTEGER2)
print("INTEGER2 :" , id(INTEGER2), type(INTEGER2), INTEGER2)

SUM_INTEGER = INTEGER1 + INTEGER2
print("Sum is: ", id(SUM_INTEGER), type(SUM_INTEGER), SUM_INTEGER)
