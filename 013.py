# ------------------------------------------------------------------------#
#                             SELECTION SORT                              #
# ------------------------------------------------------------------------#

def selection_sort(input: list[int]) -> list[int]:
    n = len(input)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if input[j] < input[min_idx]:
                min_idx = j
        tmp = input[i]
        input[i] = input[min_idx]
        input[min_idx] = tmp
    return input

x: list[int] = [4,5,9,6,1,3,6]
x = selection_sort(x)
print(x)