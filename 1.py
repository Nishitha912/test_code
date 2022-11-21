n  = int(input())
b = False
if n < 0:
    b = True
n = abs(n)
result = ""
while n>=3:
    res+=str(n%3)
    n = n//3
result = result[::-1]
result = str(n)+result

if b:
    print('-' + result)
else:
    print(result)
