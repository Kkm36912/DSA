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