# ------------------------------------------------------------------------#
#                                 FUNCTIONs                               #
# ------------------------------------------------------------------------#

# dichiara una funzione somma 
#   che prende in input due argomenti a e b di tipo int
#   che restituisce in output un valore di tipo int

# dichiara le funzioni: sottrai, dividi e moltiplica

# dichiara una funzione "concatena" che date due stringhe in input
# le concatena e ritorna in output il valore concatenato

# dichiara una funzione "divisore" che dati in input due numeri interi x e y
# controlla se x e' un divisore intero di y e ritorna il risultato 
# come valore di tipo booleano

# qual'e' la firma delle funzioni "concatena" e "divisore"?

# cos'e' print? qual'e' la firma di print?

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
#                                 IMPORT                                  #
# ------------------------------------------------------------------------#

# dal modulo sys importa la funzione getsizeof

# stampa il risultato di getsizeof(1)
