# ------------------------------------------------------------------------#
#                             BUBBLE SORT                                 #
# ------------------------------------------------------------------------#

def bubble_sort(input: list[int]) -> list[int]:
    while True:
        sorted = True
        for i in range(len(input) - 1):
            if input[i] > input[i+1]:
                tmp = input[i]
                input[i] = input[i+1]
                input[i+1] = tmp
                sorted = False
        if sorted:
            return input

x: list[int] = [4,5,9,6,1,3,6]
x = bubble_sort(x)
print(x)