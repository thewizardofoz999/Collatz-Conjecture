n = int(input("TYPE THE NUMBER IN: "))
print(n)
i = 0
while n != 1:
    if (n % 2 == 0):
        n = n/2
        print(n)
        i = i+1
    else:
        n = (3*n)+1
        print(n)
        i = i + 1
print(i)
