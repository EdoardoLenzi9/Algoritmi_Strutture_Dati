# ------------------------------------------------------------------------#
#                             ALGORITMI ORDINAMENTO                       #
# ------------------------------------------------------------------------#
def indice_numero_minimo(input: list[int]) -> int:
    n: int = len(input)
    minimo: int = input[0]
    indice_numero_minimo: int = 0
    for i in range(n):
        if input[i] < minimo:
            minimo = input[i]
            indice_numero_minimo = i
    return indice_numero_minimo

def ordina_lista(input: list[int]) -> list[int]:
    n: int = len(input)
    output: list[int] = []
    for i in range(n):
        idx_min = indice_numero_minimo(input)
        output.append(input[idx_min])
        del input[idx_min]
    return output

x: list[int] = [4,5,9,6,1,3,6]
x = ordina_lista(x)
print(x)

# quante iterazioni sono necessarie?

# questo algoritmo e' efficiente? anche con tantissimi numeri?

# come si potrebbe ottimizzare questo algoritmo per fargli fare meno istruzioni/iterazioni?
