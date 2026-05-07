# ------------------------------------------------------------------------#
#                                     FOR                                 #
# ------------------------------------------------------------------------#
# stampa i numeri nella lista
for i in [1,2,4,8,16]:
    print(i)

# stampa i numeri da 1 a 100 usando la funzione range e il ciclo for
for i in range(100):
    print(i+1)

# stampa i numeri da 10 a 100 usando la funzione range e il ciclo for
for i in range(10,101):
    print(i)

# stampa i numeri pari da 1 a 100
intervallo = range(1,101)
for i in intervallo:
    if i % 2 == 0:
        print(i)

# stampa i numeri dispari da 1 a 100 in 3 modi diversi
intervallo = range(1,101)
for i in intervallo:
    if not (i % 2 == 0):
        print(i)
    if i % 2 == 1:
        print(i)
    if i % 2 != 0:
        print(i)
# ------------------------------------------------------------------------#
#                                     WHILE                               #
# ------------------------------------------------------------------------#

# stampa i numeri da 1 a 100 usando il ciclo WHILE
i: int = 1
while i < 101:
    print(i)
    i = i + 1

# stampa i numeri da 10 a 100 usando il ciclo WHILE
i: int = 10
while i < 100 + 1:
    print(i)
    i = i + 1

# stampa i numeri pari da 1 a 100
i: int = 10
while i < 100 + 1:
    if not (i % 2 == 1):
        print(i)
    i = i + 1
