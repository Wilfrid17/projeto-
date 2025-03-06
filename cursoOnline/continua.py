'''
How to program in pyhon - chapter 3
using the continue statement.
'''
for number in range(1,11):
    if number > 5:
        continue
    print(number, end=' ')
print("\nUsed continue to skip print values grater than 5")