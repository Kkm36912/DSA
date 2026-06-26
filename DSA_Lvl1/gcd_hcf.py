#FIRST APPROACH IN BRUTE FORCE
"""def gcd(A, B):
  divisors = 0
  greatest_divisor = 0
  if A == 1 and B == 1:
      return 1
  elif A < B:
      for i in range(1,A+1):
          if A%i == 0 and B%i == 0:
              divisors = i
              greatest_divisor = max(greatest_divisor, divisors)
  else:
      for i in range(1,B+1):
          if A%i == 0 and B%i == 0:
              divisors = i
              greatest_divisor = max(greatest_divisor, divisors)
  return greatest_divisor"""

#SECOND APPROACH IN BRUTE FORCE
def gcd(A, B):
  greatest_divisor = 1
  for i in range(1, min(A,B)+1):
      if A%i == 0 and B%i == 0:
          greatest_divisor = i
  return greatest_divisor

a = int(input())
b = int(input())
print(gcd(a,b))


"""TIME COMPLEXITY IS O(min(a,b))"""