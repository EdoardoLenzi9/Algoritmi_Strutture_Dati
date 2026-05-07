# ------------------------------------------------------------------------#
#                                 FUNCTIONs                               #
# ------------------------------------------------------------------------#

# dichiara una funzione somma 
#   che prende in input due argomenti a e b di tipo int
#   che restituisce in output un valore di tipo int

def somma(a: int, b: int) -> int:
    return a + b

# dichiara le funzioni: sottrai, dividi e moltiplica
def sottrai(a: int, b: int) -> int:
    output: int = somma(a, -b)
    return output

def dividi(a: int, b: int) -> float:
    if b == 0:
        print("errore! non si divide per 0!! non siamo piu' amici!!!")
        return 0.0
    return a / b

def moltiplica(a: int, b: int) -> int:
    return a * b

# dichiara una funzione "concatena" che date due stringhe in input
# le concatena e ritorna in output il valore concatenato
def concatena(a: str, b: str) -> str:
    return f"{a}{b}"
    
# dichiara una funzione "divisore" che dati in input due numeri interi x e y
# controlla se x e' un divisore intero di y e ritorna il risultato 
# come valore di tipo booleano
def divisore(x: int, y: int) -> bool:
    return x % y == 0

# qual'e' la firma delle funzioni "concatena" e "divisore"?
def concatena(a: str, b: str) -> str:
    ...

def divisore(x: int, y: int) -> bool:
    ...

# cos'e' print? qual'e' la firma di print?
def print(input: str):
    ...

# ------------------------------------------------------------------------#
#                                 EXAMPLE                                 #
# ------------------------------------------------------------------------#

print("inizio programma")

x: int = 1
y: int = 2

def somma(x: int, y: int) -> int:
    w: int = x + y
    return w

z = somma(3, 4)

# cosa verra' stampato nelle prossime righe?
print(x)
print(y)
print(z)

# ------------------------------------------------------------------------#
#                                 IMPORT (OPZIONALE)                      #
# ------------------------------------------------------------------------#

# dal modulo sys importa la funzione getsizeof
from sys import getsizeof

# stampa il risultato di getsizeof(1)
print(getsizeof(1))