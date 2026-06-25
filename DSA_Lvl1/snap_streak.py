def longestStreak(s):
  streak_count = 0
  consecutive_count = 0
  for i in s:
      if i == '1':
          streak_count += 1
          consecutive_count = max(consecutive_count, streak_count)
      else:
          streak_count = 0
  return consecutive_count

s = input()
print(longestStreak(s))