# ------------------------------------------------------------------------#
#                             RICERCA BINARIA                             #
# ------------------------------------------------------------------------#

def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


x = [1, 3, 4, 5, 6, 6, 9]
print(binary_search(x, 6))