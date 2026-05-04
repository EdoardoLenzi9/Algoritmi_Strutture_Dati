# ------------------------------------------------------------------------#
#                                     INPUT                               #
# ------------------------------------------------------------------------#

# chiedi all'utente in input la sua eta e salvala nella variabile intera x
# usando la funzione built-in "input" 

# ------------------------------------------------------------------------#
#                                     IF                                  #
# ------------------------------------------------------------------------#

# se la variabile x >= 18 stampa "sei maggiorenne"
# se la variabile x <  18 stampa "sei minorenne"
# se la variabile x >  50 stampa "sei over cinquanta"

x: int = int(input("insersci eta: "))
if x < 18:
    print("sei minorenne")
elif x >= 18 and x < 50:
    print("sei maggiorenne")
else:
    print("sei over cinquanta")
