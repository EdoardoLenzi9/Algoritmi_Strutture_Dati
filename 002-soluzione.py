# ------------------------------------------------------------------------#
#                                 ARITMETICA BOOLEANA                     #
# ------------------------------------------------------------------------#

# dichiara una variabile "x" di tipo booleano ("bool") con valore True
x: bool = True

# dichiara una variabile "y" di tipo booleano ("bool") con valore False
y: bool = False

# stampa il valore di "x" e "y"
print(f"x={x} y={y}")

# ------------------------------------------------------------------------#
#                                 OPERAZIONI                              #
# ------------------------------------------------------------------------#

# dichiara una variable "z" di tipo booleano come x OR y e stampane il valore
z: bool = x or y
print(z)

# assegna alla variable "z" il valore y OR x e stampane il valore
z = y or x
print(z)

# assegna alla variable "z" il valore x AND y e stampane il valore
z = x and y
print(z)

# assegna alla variable "z" il valore y AND x e stampane il valore
z = y and x
print(z)

# assegna alla variable "z" il valore 1 > 2 e stampane il valore
z = 1 > 2
print(z)

# assegna alla variable "z" il valore 2 > 1 e stampane il valore
z = 2 > 1
print(z)

# assegna alla variable "z" il valore 1 <= 2 e stampane il valore
z = 1 <= 2
print(z)

# assegna alla variable "z" il valore 2 <= 1 e stampane il valore
z = 2 <= 1
print(z)

# assegna alla variable "z" il valore (2 <= 1) AND (x) OR (x AND y) e stampane il valore
z = (2 <= 1) and (x) or (x and y)
print(z)

#------------------------#
#  TABELLA DI VERITA OR  #
#------------------------#
# True or True = True
# True or False = True
# False or True = True
# False or False = False 

#------------------------#
#  TABELLA DI VERITA AND #
#------------------------#
# True and True = True
# True and False = False
# False and True = False
# False and False = False 

z: bool = True
y: bool = False
print(z and y)
print("ciao" == "hello")