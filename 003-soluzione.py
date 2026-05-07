# ------------------------------------------------------------------------#
#                                 ARITMETICA STRINGHE                     #
# ------------------------------------------------------------------------#

# dichiara una variabile "x" di tipo stringa ("str") con valore "Hello"
x: str = "Hello"

# dichiara una variabile "y" di tipo stringa ("str") con valore "World!"
y: str = "World!"

# stampa il valore di "x" e "y"
print(x)
print(y)

# dichiara due stringhe in-linea utilizzando le 2 dichiarazioni ammesse: "...", '...'
a: str = "Hello"
b: str = 'Hello'

# dichiara due stringhe multi-linea utilizzando le 2 dichiarazioni ammesse: """...""", '''...'''
c: str = """
            Hello
            World!
        """
d: str = '''
            Hello
            World!
        '''

# ------------------------------------------------------------------------#
#                                 SLICING e OPERAZIONI                    #
# ------------------------------------------------------------------------#

# dichiara una variable "z" di tipo stringa come concatenazione di x e y (con uno spazio in mezzo) 
z: str = x + " " + y

# ridichiara "z" usando "string format" (f"") per concatenare x e y
z = f"{x} {y}"

# stampa il primo carattere di z
print(z[0])
print(z[0:1])
print(z[ :1])

# stampa il secondo carattere di z
print(z[1])
print(z[1:2])

# stampa i primi due caratteri di z
print(z[0:2])
print(z[ :2])

# stampa l'ultimo carattere di z
print(z[-1:            ])
print(z[-1:len(z)      ])
print(z[len(z)-1:      ])
print(z[len(z)-1:len(z)])

# stampa gli ultimi tre caratteri di z
print(z[-3:])

# concatena i primi tre caratteri di z agli ultmi due, salva il valore in w e stampa la variabile w
w:str = f"{z[:3]}{z[-2:]}"
print(w)

# dichiara una variabile booleana b come confronto fra w e "Held!"
b: bool = w == "Held!"
print(b)

# assegna alla variabile booleana b il confronto fra w e "He!"
b = "He!" == b
print(b)

# assegna alla variabile booleana b il confronto "w contiene la sottostringa "World" usando l'operatore in
b = "World" in w
print(b)