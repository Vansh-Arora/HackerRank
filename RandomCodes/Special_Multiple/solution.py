num = int(input())
i = 1
while( int(str(bin(i)[2:].replace("1","9"))) % num != 0):
    i += 1
print(int(str(bin(i)[2:].replace("1","9"))))