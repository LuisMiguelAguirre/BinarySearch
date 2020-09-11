def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2

        if item == list[mid]:
            return mid
        if item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 2, 4, 5, 7]

print(binary_search(list, 1))
print(binary_search(list, 2))
print(binary_search(list, 4))
print(binary_search(list, 5))
print(binary_search(list, 7))
print(binary_search(list, 0))
print(binary_search(list, 8))