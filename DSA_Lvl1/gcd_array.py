def gcd(N, arr):
  if N == 1:
      return arr[0]
  elif N == 2:
      while (arr[0] != 0 and arr[1] != 0):
          if arr[0] >= arr[1]:
              arr[0] = arr[0]%arr[1]
          else:
              arr[1] = arr[1]%arr[0]
      if arr[0] == 0:
          return arr[1]
      else:
          return arr[0]
  else:
      gcd_arr =arr[:2]
      while (gcd_arr[0] != 0 and gcd_arr[1] != 0):
          if gcd_arr[0] >= gcd_arr[1]:
              gcd_arr[0] = gcd_arr[0]%gcd_arr[1]
          else:
              gcd_arr[1] = gcd_arr[1]%gcd_arr[0]
      if gcd_arr[0] == 0:
          arr = arr[2:]
          arr.append(gcd_arr[1])
          N -= 1
          return gcd(N, arr)
      else:
          arr = arr[2:]
          arr.append(gcd_arr[0])
          N -= 1
          return gcd(N, arr)
      
N = int(input("Enter array length:- "))
arr_input = input()
arr = list(map(int, arr_input.split(" ")))
print(gcd(N,arr))

