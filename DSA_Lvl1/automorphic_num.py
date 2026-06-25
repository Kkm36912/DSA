def checkAutomorphicNumber(num):
  square = str(num**2)
  str_num = str(num)
  backward = len(str_num)
  for i in range(0,len(str_num)):
      if str_num[i] == square[-backward]:
          backward -= 1
          continue
      else:
          return False
  return True

num = int(input())
result = checkAutomorphicNumber(num)
print(result)

"""Automorphic number is a number whose square ends with the same digits as number itself eg:- 76**2 = 5776 so here 5776 ends with 76 so 76 is a automorphic number"""