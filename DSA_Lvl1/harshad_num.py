def checkHarshadNumber(num):
  num_list = list(map(int, list(str(num))))
  divisor = 0
  for each in num_list:
    divisor += each
  if num%divisor == 0:
    return True
  else:
    return False
  
num = int(input())
result = checkHarshadNumber(num)
print(result)

"""Harshad number is a number whose sume of each digit is a number which is the divisor of the same number eg:- 156 where 1 + 5 + 6 is 12 which is a divisor of 156 so it's a harshad number"""