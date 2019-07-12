m=input()
m=m.split()
m1=m[0]
m2=m[1]
count=0
i=0
while(i<len(m1) and count<2):
    if(m1[i]!=m2[i]):
        count+=1
    i+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
