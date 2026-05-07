# ------------------------------------------------------------------------#
#                            FUNZIONI STRINGHE                            #
# ------------------------------------------------------------------------#

# le stringhe sono un tipo di dato complesso che 
# include molte funzioni/metodi di utilita',
# qui vediamo i piu' famosi e utilizzati

# len() calcola la lunghezza di una stringa o di una lista 
s: str = "Hello World!"
l: int = len(s)
print(f"Lunghezza della stringa '{s}': {l} caratteri")

# lower() trasforma i caratteri maiuscoli in minuscolo
print(s.lower())

# upper() trasforma i caratteri minuscoli in maiuscolo
print(s.upper())

# capitalize() trasforma la prima lettera in maiuscolo
print("hello world!".capitalize())

# replace() rimpiazza tutte le occorrenze di una sotto-stringa
# con una nuova stringa
x: str = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidunt ut labore et dolore magna aliqua'''
y: str = x.replace("a", "🐊")
y: str = y.replace("e", "🐘")
y: str = y.replace("i", "🦛").replace("o", "🦢")
y.replace("u", "🦄")
print(y)

# .isalpha() .isdigit() tornano un booleano nel caso in cui la stringa contenga 
# solo caratteri alfabetici o cifre numeriche
x: str = "123"
if x.isdigit():
    y: int = int(x)
y: str = "abc"
if y.isalpha():
    print(y)

# .strip() rimuove i caratteri "blank" all'inizio e alla fine
# (per esempio spazi, tab, a capo)
print(" \n    a b c \n".strip())

# count() conta le ricorrenze di una sotto-stringa in una stringa
numero_di_a: int = "abcabbccd".count("a")
print(numero_di_a)

# find() trova l'indice di una sotto-stringa in una stringa
indice_di_world: int = "hello world!".find("world")
print(indice_di_world)

# ------------------------------------------------------------------------#
#              ESERCIZIO SFIDANTE MA CHE TI FA MOLTO BENE!                #
# ------------------------------------------------------------------------#

# dichiarare una funzione main() senza input e senza output
# nella funzione main richiedere all'utente in input una stringa con il suo nome e cognome
# usara la funzione lower() per trasformare la stringa in minuscolo
# usare un ciclo while per trasformare solo il primo carattere del nome e del cognome in maiuscolo
# stampare la stringa
# invocare la funzione main
def main():
    nome: str = input("inserisci nome e cognome: ")
    nome = nome.lower()
    i: int = 0
    nome = nome.capitalize()
    while i < len(nome):
        if nome[i] == " ":
            nome = nome[:i+1] + nome[i+1].upper() + nome[i+2:]
        i += 1
    print(nome)

main()

# ------------------------------------------------------------------------#
#     ESERCIZIO CHE SE LO FAI TI ASSUMONO A IN GOOGLE DOMANI MATTINA!     #
# ------------------------------------------------------------------------#

# generare automaticamente un calendario di questo tipo per l'anno 2026
# sapendo che 01/01/2026 era un giovedi:
# gio 01/01/2026
# ven 02/01/2026
# sab 03/01/2026
# ...
# sab 31/01/2026
# dom 01/02/2026
# ...
# gio 31/12/2026

def stampa_calendario():
    anno: int = 2026
    contatore_giorni = 1
    for mese in range(1,13):
        for giorno in range(1,32):
            if (
                (mese == 1 and giorno <= 31) or
                (mese == 2 and giorno <= 27) or
                (mese == 3 and giorno <= 31) or
                (mese == 4 and giorno <= 30) or
                (mese == 5 and giorno <= 31) or
                (mese == 6 and giorno <= 30) or
                (mese == 7 and giorno <= 31) or
                (mese == 8 and giorno <= 31) or
                (mese == 9 and giorno <= 30) or
                (mese == 10 and giorno <= 31) or
                (mese == 11 and giorno <= 30) or
                (mese == 12 and giorno <= 31)
            ):
                etichetta = "dom"
                if contatore_giorni % 7 == 1:
                    etichetta = "lun"
                if contatore_giorni % 7 == 2:
                    etichetta = "mar"
                if contatore_giorni % 7 == 3:
                    etichetta = "mer"
                if contatore_giorni % 7 == 4:
                    etichetta = "gio"
                if contatore_giorni % 7 == 5:
                    etichetta = "ven"
                if contatore_giorni % 7 == 6:
                    etichetta = "sab"
                print(f"{etichetta} {giorno}/{mese}/{anno}")
                contatore_giorni += 1

stampa_calendario()

# ------------------------------------------------------------------------#
#  ESERCIZIO DA FARE MENTRE ASPETTI DI ENTRARE IN GOOGLE DOMANI MATTINA!  #
# ------------------------------------------------------------------------#

# scrivere una funzione inverti_stringa che data una stringa in input la 
# inverte e la ritorna in output. Stampare la stringa

def inverti_stringa(stringa: str) -> str:
    invertita = ""
    for i in range(1,len(stringa) + 1):
        invertita += stringa[-i]
    return invertita

print(inverti_stringa("Hello World!"))