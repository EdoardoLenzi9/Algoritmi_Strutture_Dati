# ------------------------------------------------------------------------#
#                LIST, LIST COMPREHENSION, SET, DICT, TUPLE               #
# ------------------------------------------------------------------------#

# inizializza una lista con i numeri da 1 a 100 usando un ciclo for

x: list[int] = []
for i in range(1,101):
    x.append(i)

# inizializza una lista con i numeri da 1 a 100 usando un ciclo while

x: list[int] = []
i: int = 1
while i < 101:
    x.append(i)
    i += 1

# inizializza una lista con i numeri da 1 a 100 usando range e ciclo for

x: list[int] = []
for i in range(1,101):
    x.append(i)

# inizializza una lista con i numeri da 1 a 100 usando range ebbbbasta

x: list[int] = list(range(1,101))

# data una lista con i numeri da 1 a 100 stampala

print(x)

# data una lista `x` con i numeri da 1 a 100 stampa una lista con tutti i numeri raddoppiati (2,4,6,8...)

for i in x:
    print(i * 2)

# rifai l'esercizio ma usa la list comprehension per raddoppiare i numeri e generare la lista y poi stampala

x = list(range(1,101))
y = [i*2 for i in x]
print(y)

# usa la list comprehension su y per eliminare dalla lista tutti i multipli di 10, salva in z e stampala

z = [i for i in y if i % 10 != 0]
print(z)

# converti la lista x = [1,1,2,3] in un set
# fai CRUD sul set usando le sue funzioni primitive (push, pop, ...)
# trasforma il set in lista
# fai CRUD sulla lista usando le sue funzioni primitive

# dichiara un dizionario a chiavi intere e valori stringa vuoto

# dichiara un dizionario a chiavi stringa e valori interi con questi valori iniziali
# "a": 1, "b": 2, "c": 3
# fai CRUD sul dizionario usando le sue funzioni primitive
# stampa le chiavi, salvale in una lista
# stampa i valori, salvali in una lista
# stampa il valore di "b", stampa la chiave di 3, cerca un valore che non esiste

# prova a filtrare il set e il dizionario degli esercizi sopra usando set e dict comprehension

# inizializza una tupla a due valori 1,2
# usa il pattern matching per assegnare con una sola riga di codice i valori della tupla alle variabili x e y
# aggiungi alla tupla altri valori
# fai CRUD sulla tupla# 01. inizializza una lista con i numeri da 1 a 100 usando un ciclo for

...

# inizializza una lista con i numeri da 1 a 100 usando un ciclo while

...

# inizializza una lista con i numeri da 1 a 100 usando range e ciclo for

...

# inizializza una lista con i numeri da 1 a 100 usando range ebbbbasta

...

# data una lista con i numeri da 1 a 100 stampala

...

# data una lista `x` con i numeri da 1 a 100 stampa una lista con tutti i numeri raddoppiati (2,4,6,8...)

x = ...

# rifai l'esercizio 06 ma usa la list comprehension per raddoppiare i numeri e generare la lista y poi stampala

x = ...
y = ...
print(y)

# usa la list comprehension su y per eliminare dalla lista tutti i multipli di 10, salva in z e stampala

x = ...
y = ...
z = ...
print(z)
