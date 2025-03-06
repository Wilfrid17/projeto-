"""
How to program in python - chapter 3.

Exempl e of structural pattern matching.
###########################################
Examination result exemple using ther structural pattern matching
for testing multiple option
"""
GRADE_A = 0
GRADE_B = 0
GRADE_C = 0
GRADE_D = 0
COUNTER = 1

while COUNTER <= 10:
    RESULT = input("Enter result (A,B,C or D)")

    match RESULT:
        case "A":
            GRADE_A = GRADE_A + 1
        case "B":
            GRADE_B = GRADE_B + 1
        case "C":
            GRADE_C = GRADE_C + 1
        case "D":
            GRADE_D = GRADE_D + 1

    COUNTER = COUNTER + 1
print("GRADE A %", GRADE_A / COUNTER * 100)
print("GRADE B %", GRADE_B / COUNTER * 100)
print("GRADE C %", GRADE_C / COUNTER * 100)
print("GRADE D %", GRADE_D / COUNTER * 100)