n=int(input())
a=[]
b=[]
for i in range(n):
    arr=list(map(int, input().split()))
    a.append(arr[0])
    b.append(arr[1])

max=0
curr=0
for i in range(n):
    curr= curr+(-a[i]+b[i])
    #print(curr)
    if curr>max:
        max=curr

print(max)
