print("Collatz Series Finder")

endnumber = int(input("The largest number to be tested:  "))

num = 1
unum = 1

sit = num % 2

i = 0
recnum = 0
reclenght = 0

while unum < endnumber:
    unum = unum + 1
    num = unum
    sit = num % 2
    while (num != 1) and (num != 0):

        while (sit == 1) and (num != 0):
            num = num * 3 + 1
            i = i + 1
            sit = num % 2

        while (sit == 0) and (num != 0):
            num = num / 2
            i = i + 1
            sit = num % 2

    if i > reclenght:
        reclenght = i
        recnum = unum
        i = 0
    else :
        i = 0

itest = 0
n = recnum
while n != 1:
    if (n % 2 == 0):
        n = n/2
        itest = itest+1
    else:
        n = (3*n)+1
        itest = itest + 1

print(recnum)
print(itest)
