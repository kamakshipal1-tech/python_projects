n=int(input("Enter the number"))
arr=[]
for _ in range(n):
    arr.append(int(input("Enter the number")))
    unique=sorted(list(set(arr)))
    if (len(unique)>1):
        sh=unique[-2]
     print(sh)
