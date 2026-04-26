# ------------------------------------------------------------------------#
#                             ALGORITMI RICERCA                           #
# ------------------------------------------------------------------------#

def ricerca_indice(lista: list[int], chiave_di_ricerca: int) -> int:
    n = len(lista)
    for i in range(n):
        if lista[i] == chiave_di_ricerca:
            return i
    return -1

x: list[int] = [1,3,6,7,9,15,32,67,82,99]
i = ricerca_indice(x, 32)
if i > 0:
    print(f"elemento {x[i]} in posizione {i}")
else:
    print("elemento non trovato")
