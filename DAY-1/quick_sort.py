arr = [3,5,1,2,9,8,7]
def partition(arr,low,high):
  pivot = arr[low]
  i = low
  j = high
  while i < j:
    while arr[i] <= pivot and i <= high - 1:
      i+=1
    while arr[j] >= pivot and j >= low+1:
      j-=1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
  arr[low], arr[j] = arr[j], arr[low]
  return j

def quick_sort(arr, low , high):
  if low < high:
    part_index = partition(arr,low,high)
    quick_sort(arr, low, part_index-1)
    quick_sort(arr, part_index + 1, high)
  return arr

low = 0
high = len(arr) - 1

print(quick_sort(arr,low,high))
"""
TIME COMPLEXITY IN BEST/AVERAGE CASE IS O(NlogN)
TC IN WORST CASE IS O(N^2)    e.g. arr=[3,3,3,3,3,3,3,3]

SPACE COMPLEXITY IS O(1)

BETTER THAN MERGE SORT BUT NOT IN WORST CASE
"""