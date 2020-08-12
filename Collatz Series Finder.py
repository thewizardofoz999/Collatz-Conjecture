import winsound

print("Collatz Series Finder")

endnumber = int(input("The largest number to be tested:  "))

num = 1
unum = 1

sit = num % 2

i = 0
recnum = 0
reclength = 0

while unum < endnumber:
    unum = unum + 1
    num = unum
    sit = num % 2
    while (num != 1) and (num != 0):

        while (sit == 1) and (num != 0):
            num = (num * 3 + 1)/2
            i = i + 2
            sit = num % 2

        while (sit == 0) and (num != 0):
            num = num / 2
            i = i + 1
            sit = num % 2

    if i > reclength:
        reclength = i
        recnum = unum
        i = 0
    else :
        i = 0


# Test algorithm starts here.

itest = 0
n = recnum
while n != 1:
    if (n % 2 == 0):
        n = n/2
        itest = itest+1
    else:
        n = ((3*n)+1)/2
        itest = itest + 2

if reclength == itest:
    print("Successful")
    print("Number: ",recnum)
    print("Length: ",itest)


# Test algorithm ends here.

frequency = 1500
duration = 500
winsound.Beep(frequency, duration)
