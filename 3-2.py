n,m,k = list(map(int,input().split()))

data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    else:
      result += first
      m = m-1
  if m == 0:
      break
  result += second
  m = m-1

print(result)
