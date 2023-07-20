def printTo(n):
    if n==1:
        print(1,end='\t')
        return 0
    else:
        printTo(n-1)
        print(n,end='\t')
        return 0
printTo(int(input()))