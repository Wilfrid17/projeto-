""" 
How to program in python - chapter 4
Finding the maximum of integers
using keyboard entry
"""

def maximum_values(x_value,y_value,z_value):
    '''''Maximum values betwen three numbers'''
    maximum = x_value
    if y_value > maximum:
        maximum = y_value
        
    if x_value > maximum:
        maximum = z_value
        
    return maximum

A_VALUE = int(input("Enter the first value: "))
B_VALUE = int(input("Enter the second value: "))
C_VALUE = int(input("Enter the third value: "))

# fuction call
print("Maximum value is: ", maximum_values(A_VALUE,B_VALUE,C_VALUE))
print() # print new line

D_VALUE = int(input("Enter the first value: "))
E_VALUE = int(input("Enter the second value: "))
F_VALUE = int(input("Enter the third value: "))

print("Maximum value is: ", maximum_values(D_VALUE,E_VALUE,F_VALUE))
print() # print new line

G_VALUE = int(input("Enter the first value: "))
H_VALUE = int(input("Enter the second value: "))
I_VALUE = int(input("Enter the third value: "))

print("Maximum value is: ", maximum_values(G_VALUE,H_VALUE,I_VALUE))
print() # print new line