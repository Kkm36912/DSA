arr= [5,7,8,1,2,6,4]
n = len(arr)
for i in range(0,n-1):
  min_index = i
  for j in range(i+1,n):
    if arr[j] < arr[min_index]: #TO GO FOR DESCENDING ORDER JUST DO arr[j] > arr[min_index]
      min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

#TIME COMPLEXITY IS O(N(N+1)/2 i.e. Sum of n terms) EQUIVALENT TO O(N^2)
#SPACE COMPLEXITY IS O(1) SINCE WORKED ON THE SAME ARRAY AND ALSO THE VARIABLE COUNT REMAINS THE SAME DESPITE THE ARRAY LENGTH