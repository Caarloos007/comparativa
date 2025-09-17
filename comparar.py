import time, random

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

data = [random.randint(0, 1000) for _ in range(2000)]
for algo in [bubble_sort, quick_sort]:
    start = time.time()
    algo(data.copy())
    print(algo.__name__, time.time() - start)