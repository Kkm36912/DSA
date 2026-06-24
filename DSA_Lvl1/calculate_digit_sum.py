def calculateDigitSum(N1, N2):
  digit_sum = 0
  for num in range(N1,N2+1):
    each_digit_list = list(map(int, list(str(num))))
    for each in each_digit_list:
      digit_sum += each
  return digit_sum

n1 = int(input())
n2 = int(input())
result = calculateDigitSum(n1,n2)
print(result)