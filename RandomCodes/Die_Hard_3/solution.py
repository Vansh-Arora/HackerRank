a = int(input())
b = int(input())
n = int(input())
ans = "no"
if a>b:
    big = a
    small = b
else:
    big = b
    small = a
while( abs(big - small) != small ):
    if n % (big-small) == 0:
        ans = "yes"
        break
    else:
        big = big-small  
print(ans)