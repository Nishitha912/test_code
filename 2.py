def count(s,c) : 
    result = 0
    for i in range(len(s)):
        if (s[i] == c):
            result = result + 1
    return result
string1=input()
string2=input()
c = string2[-1]
print(count(string1,c))
