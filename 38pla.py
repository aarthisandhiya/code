#ezhil
n=int(input())
lis=[]
res=''
for i in range(1,n+1):
    if n%i==0 and i%2==0 :
        res=res+str(i)+' '
print(res.strip())
        
        
