#weird-n is odd n is even between 6 to 20
#notweird- n is even and between 2 &5 (even and greater than 20)
n=int(input())
if n%2==0 and 2<=n<=5 or n%2==0 and n>20:
    print("Not Weird")
else:
    print("Weird")