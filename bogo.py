from random import shuffle

# Verifying if array is sorted
def isSorted(arr):
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False
    return True


# BOGO Sort
def bogo(arr):
    while not isSorted(arr):
        shuffle(arr)


wallahi = [4, 2, 3, 5, 1]
bogo(wallahi)
