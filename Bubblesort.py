def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = list(map(int, input("Enter elements for array: ").strip().split()))
bubble_sort(arr)
print(arr)
