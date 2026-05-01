arr = [3,5,6,4,8,2]
n = len(arr)
#ASSUMING THE SINGLE ELEMNT OF THE ARRAY WILL BE SORTED THAT'S STARTED FROM 1 NOT 0
for i in range(1,n):
  key = arr[i]
  j = i - 1
  while j >= 0 and key < arr[j]:
    arr[j+1] = arr[j]
    j -= 1
  arr[j+1] = key 
print(arr)


'''TIME COMPLEXITY IS O(N(N+1)/2 i.e. Sum of n terms) EQUIVALENT TO O(N^2)
SPACE COMPLEXITY IS O(1)'''