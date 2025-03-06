"""
HOW TO PROGRAM IN PYTHON -chapter
String formatting demostration
"""
print("The LORD is my shepherd; I shall not want. 'Psalm 23:1'")
print("The LORD is my shepherd; I shall not want. \"Psalm 23:1\"")
print('The LORD is my shepherd; I shall not want. \'Psalm 23:1\'')
print('The LORD is my shepherd; I shall not want. "Psalm 23:1"')

INTEGER_VALUE = 4237.05
print("integer", INTEGER_VALUE)#imprimir sem formatação
print("Decimal integer {:.0f}".format(INTEGER_VALUE))#corta ponto decimais
print("Hexadecimal integer {:x}". format(int(INTEGER_VALUE)))#convertendo em valor inteiro formatado em hexadecimal
print("Rigth justify integer {:8d}".format(int(INTEGER_VALUE)))#valor convetido em inteiro com 8 caso no lado direito
print("Left jstify integer {%-8d}\n" % INTEGER_VALUE)#formata valor em porcentagem e alinha a esqueda com 8 espaço

FLOAT_VALUE = 4237.05
print("Float", FLOAT_VALUE)
print("Default float {:f}".format(FLOAT_VALUE))
print("Default exponential float {:e}\n".format(FLOAT_VALUE))

STRING_VALUE = "String formattig"
print("Force eightn digits in integer %.8d" %INTEGER_VALUE)
print("Five digits after decimal in float %.5f" % FLOAT_VALUE)
print("Fifteen and five characters allowed in string:")
print("{:.15s}".format(STRING_VALUE))
print("{:.5s}".format(STRING_VALUE))

