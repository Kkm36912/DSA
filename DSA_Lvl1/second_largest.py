def secondLargestDigit(num):
  first_largest = -1
  second_largest = -1
  str_num = str(num)
  for digit in str_num:
      if int(digit) > first_largest:
          second_largest = first_largest
          first_largest = int(digit)
      elif int(digit) > second_largest and int(digit) < first_largest:
          second_largest = int(digit)
  if second_largest == -1:
      return -1
  else:
      return second_largest

num = int(input())
result = secondLargestDigit(num)
print(result)