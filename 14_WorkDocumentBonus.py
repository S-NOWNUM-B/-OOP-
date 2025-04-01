import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

random_numbers = [random.randint(1, 10000) for _ in range(5000)]

with open("numbers.txt", "w") as f:
    f.write(" ".join(map(str, random_numbers)))

bubble_arr = random_numbers.copy()
quick_arr = random_numbers.copy()
merge_arr = random_numbers.copy()

start_time = time.time()
bubble_sort(bubble_arr)
bubble_time = time.time() - start_time

start_time = time.time()
quick_sort(quick_arr)
quick_time = time.time() - start_time

start_time = time.time()
merge_sort(merge_arr)
merge_time = time.time() - start_time

print(f"Время пузырьковой сортировки: {bubble_time:.4f} секунд")
print(f"Время быстрой сортировки: {quick_time:.4f} секунд")
print(f"Время сортировки слиянием: {merge_time:.4f} секунд")

if bubble_time < quick_time and bubble_time < merge_time:
    print("\nПузырьковая сортировка оказалась самой быстрой")
elif quick_time < bubble_time and quick_time < merge_time:
    print("\nБыстрая сортировка оказалась самой быстрой")
else:
    print("\nСортировка слиянием оказалась самой быстрой")