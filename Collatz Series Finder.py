print("Collatz Series Finder")

mogrnu = input("The largest number to be tested:  ")


bitissayisi = int(mogrnu)

sayi = 1
usayi = 1

sit = sayi % 2

i = 0
kayitsayi = 0
kayitsefer = 0

while usayi < bitissayisi:
    usayi = usayi + 1
    sayi = usayi
    sit = sayi % 2
    print(sayi)
    while (sayi != 1) and (sayi != 0):

        while (sit == 1) and (sayi != 0):
            sayi = sayi * 3 + 1
            i = i + 1
            sit = sayi % 2

        while (sit == 0) and (sayi != 0):
            sayi = sayi / 2
            i = i + 1
            sit = sayi % 2

    if i > kayitsefer:
        kayitsefer = i
        kayitsayi = usayi
        i = 0
    else :
        i = 0

print(kayitsayi)
print(kayitsefer)
