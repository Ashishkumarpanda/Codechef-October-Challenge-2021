t = int(input())
for i in range(t):
    l = list(map(int,input().split(" ")))
    if l[0]>0 and l[1]>0:
        print("Solution")
    elif l[0] == 0:
        print("Liquid")
    elif l[1]==0:
        print("Solid")
