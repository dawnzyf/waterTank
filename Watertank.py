#Created by Dawn
print('Please input the length of each label(m), split by " "： ')
lst=input().split(' ')
for i in range(len(lst)):
    lst[i]=int(lst[i])
k=1
sum1=0
while k<len(lst):
    if k==len(lst)-1:
        if lst[k]>lst[k-1]:
            sum1+=lst[k-1]
            break
        else:
            sum1+=lst[k]
            break
    if lst[k]>=lst[k-1]:
        sum1+=lst[k-1]
        k+=1
    else:
        cut=max(lst[k:])
        t=lst[k:].index(cut)
        sum1+=min([cut,lst[k-1]])*(t+1)
        k+=t+1
print('These labels can hold',sum1,'m³ of water in total.')
        
