# ------------------------------------------------------------------------#
#                                     LISTE                               #
# ------------------------------------------------------------------------#

# cos'e' una sequenza?

response = "una sequenza e' un insieme ordinato di elementi"

# cos'e' una lista/array?

response = "una lista e' una sequenza di variabili"

# quanto spazio in memoria RAM occupa una stringa?
# [ ] A. 1Byte
# [X] B. 1Byte per ogni carattere
# [ ] C. 1KiloByte per ogni carattere

# inizializza una lista x vuota, y contentente la stringa "abc", z contentente i caratteri "abc"

x = []
y = ["abc"]
z = ['a', 'b', 'c']

# misura quanto spazio occupano x, y, z 
from sys import getsizeof
ram_space = getsizeof(x) + getsizeof(y) + getsizeof(z)

# operazioni sulle liste
# - inizializza una lista di stringhe vuota x
# - controlla l'id di x
# - sovrascrivi x con una nuova lista contentente una solo valore "a"
# - controlla l'id di x (dovrebbe essere cambiato)
# - aggiungi ad x un nuovo valore "b" (senza reinizializzare la lista)
# - controlla l'id di x (dovrebbe essere lo stesso)
# - modifica l'ultimo valore in x aggiungendo i caratteri "cd"
# - stampa il primo e l'ultimo valore in x
# - rimuovi l'ultimo valore in x (tramite indice)
# - aggiungi ad x l'array ["e", "f", ["g", "h"]]
# - conta il numero di elementi in x
# - pulisci x (clear)

x: list[str] = []
print(id(x))
x = ["a"]
print(id(x))
x.append("b")
print(id(x))
x[-1] = x[-1]+"cd"
print([x[1], x[-1]])
del x[-1]
x.append(["e", "f", ["g", "h"]])
print(len(x))
x.clear()

# inizializza una lista x contenente questi valori eterogenei "a", "1", 1, True, 3.14

x = ["a", "1", 1, True, 3.14]

# inizializza una matrice bidimensionale contenente questi valori
#
#   1 0 0
#   0 1 0
#   0 0 1
#
# stampa i valori in posizione (0,0), (1,1), (-1, -1)
m:list[list[int]] = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
] 
print(m[0][0])
print(m[1][1])
print(m[-1][-1])

# salva in una matrice i valori di questa tabella
#
# titolo_libro, costo, disponibile_in_magazzino, anno_pubblicazione
# -----------------------------------------------------------------
# aaa,          1.50,   si,                      2015
# bbb,          23.0,   no,                      2016
# ccc,          4.12,   si,                      1997
m:list[list[int]] = [
    ["aaa", 1.50, True,  2015],
    ["bbb", 23.0, False, 2016],
    ["ccc", 4.12, True,  1997]
] 