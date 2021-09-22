
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)  # Slicing the list from mid+1 to end
            else:
                return recursive_binary_search(list[:midpoint], target)  # # Slicing the list from start to mid


def verify(result):
    print("Target found : ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 100)
verify(result)
