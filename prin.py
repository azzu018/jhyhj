n,m=map(int,input().split())
z=0
for i in range (n,m+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else: 
        z+=1
print(z)
