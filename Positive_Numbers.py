def  separation(x):
  y = []
  for i in x:
    if i > 0:
      y.append(i)
  return y

print(separation([1, -12, 31, 43, 5, -56]))
