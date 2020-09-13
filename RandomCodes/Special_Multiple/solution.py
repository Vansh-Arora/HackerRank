def SpecialMultiple(num):
    i = 1
    while( int(str(bin(i)[2:].replace("1","9"))) % num != 0):
        i += 1
    print(int(str(bin(i)[2:].replace("1","9"))))


T = int(input())
for i in range(T):
    num = int(input())
    SpecialMultiple(num)