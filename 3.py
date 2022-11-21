n = int(input())
invalid = ['3','4','7']
def valid(n):
    for i in str(n):
        if i in invalid:
            return False
    return True
if n > 0:
    cnt = 0
    temp = 1
    while(cnt!= n):
        if valid(temp):
            cnt+= 1
        temp+= 1
    print(temp-1)
