"""Using Euclidean Theorem which states gcd(a,b) = gcd(a-b, b) where a >= b.
However we are using Euclidean Extended theorem that states almost same formula but skips some steps so it is like gcd(a,b) = gcd(a%b, b) where a >= b if b >= a then formula becomes gcd(a,b) = gcd(a, b%a). The greatest common divisor is the last non zero value left from either of the digits a and b
"""
def euclideanTheorem(a,b):
  while(a != 0 and b != 0):
    if (a >= b):
      a = a%b
    else:
      b = b%a
  if a == 0:
    return b
  else:
    return a
  
a = int(input())
b = int(input())
print(euclideanTheorem(a,b))

"""TIME COMPLEXITY IS O(log(min(a,b)))"""