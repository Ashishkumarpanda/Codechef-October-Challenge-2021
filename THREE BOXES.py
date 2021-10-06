t = int(input())
for i in range(t):
    l = list(map(int,input().split(" ")))
    k = l[:3]
    d = l[3]
    sum = 0
    count = 0
    for i in k:
        sum = sum+i
        if sum > d:
            count = count+1
    print(count+1)
