z=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(z):
  if b[i]==i:
    c.append(i)
    c.sort()
if(len(c)==0):
  print("-1")
else:
  print(' '.join(map(str,c)))
