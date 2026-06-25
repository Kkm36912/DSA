def minimumTransfers(A, B):
  if A == 1 and B == 1:
      return 0
  marble_moved = float('inf')
  Total = A+B
  for i in range(1,Total):
      B = Total - i
      if  B != 0 and i%B == 0:
          marble_moved = min(marble_moved,abs(A-i))
  return marble_moved

a = int(input())
b = int(input())
lowest_marble_count = minimumTransfers(a,b)
print(lowest_marble_count)