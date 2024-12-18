from random import shuffle

# Verifying if array is sorted
def isSorted(arr: list[int]) -> bool:
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False
    return True

# BOGO Sort
def bogo(arr: list[int]) -> None:
    while not isSorted(arr):
        shuffle(arr)

if __name__ == "__main__":
    arr = [4, 2, 3, 5, 1]
    bogo(arr)
    print(arr)
