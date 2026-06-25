def sumOfDigits(num):
  str_num = str(num)
  if len(str_num) == 1:
      return int(str_num)
  sum_digits = 0 
  for each in str_num:
      sum_digits += int(each)
  return sumOfDigits(sum_digits)

num = int(input())
print(sumOfDigits(num))
