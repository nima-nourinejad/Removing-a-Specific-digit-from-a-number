def numshekan (x,n):
  x=str (x)
  l= len(x)
  a=[]
  c=[]
  r=''
  for i in x:
    a.append(i)
  b=a.count(str(n))
  for i in range(b):
    a.remove(str(n))
    for j in range (l-i-1):
      r=r+a[j]
    print (r)
    r=''
