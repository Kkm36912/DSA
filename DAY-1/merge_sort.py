arr = [3,1,2,5,6,2,4,5,1,9,7]
def merged_sorted_arr(left,right):
  n,m = len(left), len(right)
  i,j = 0,0
  sorted_arr = []
  while i < n and j < m:
    if left[i] <= right[j]:
      sorted_arr.append(left[i])
      i+=1
    else:
      sorted_arr.append(right[j])
      j+=1
  if i < n:
    while i < n:
      sorted_arr.append(left[i])
      i+=1
  if j < m:
    while j < m:
      sorted_arr.append(right[j])
      j+= 1
  return sorted_arr

def merge_sort(arr):
  if len(arr) == 1:
    return arr
  mid = len(arr)//2
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  left = merge_sort(left_arr)
  right = merge_sort(right_arr)
  return merged_sorted_arr(left,right)
  #TO CHANGE THE ORIGINAL ARRAY ONLY GO FOR arr[:] = merged_sorted_arr(left,right) and then return arr[:]

print(merge_sort(arr))

"""
TIME COMPLEXITY O(NlogN) AND SPACE COMPLEXITY O(N)
"""