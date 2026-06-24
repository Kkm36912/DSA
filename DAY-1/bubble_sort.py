arr = [5,8,1,2,9]
n = len(arr)
for i in range(n-2,-1,-1): #BACKWARD INDEXING
  for j in range(0,i+1):
    if arr[j] > arr[j+1]:  #FOR DESCENDING ORDER JUST DO arr[j] < arr[j+1]
      arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

'''*****FOR AVERAGE AND WORST CASE*****
TIME COMPLEXITY IS O(N(N+1)/2 i.e. Sum of n terms) EQUIVALENT TO O(N^2)
SPACE COMPLEXITY IS O(1) SINCE WORKED ON THE SAME ARRAY AND ALSO THE VARIABLE COUNT REMAINS THE SAME DESPITE THE ARRAY LENGTH'''

'''-----FOR BEST CASE MAKING AN OPTIMIZATION-----
arr = [5,8,1,2,9]
n = len(arr)
for i in range(n-2,-1,-1):
  is_swap = False         #A checker that turns true if swapping will be done in first iteration only
  for j in range(0,i+1):
    if arr[j] > arr[j+1]:  
      arr[j], arr[j+1] = arr[j+1], arr[j]
      is_swap = True
  if is_swap == False:    #If the checker remains false terminate the loop as array is already sorted
    break/return
print(arr)

TIME COMPLEXITY IS O(N) AND SPACE COMPLEXITY IS O(1)
'''