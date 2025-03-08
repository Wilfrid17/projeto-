""" 
How to program in python - chapter 4
Finding the maximum of integers
using keyboard entry
"""

def maximum_values(x_value,y_value,z_value): # function definition
    '''''Maximum values betwen three numbers'''
    maximum = x_value # assume x is the longest value
    if y_value > maximum: # if y is greater than x
        maximum = y_value # y is the longest value
        
    if x_value > maximum: # if z is greater than x
        maximum = z_value # z is the longest value
        
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