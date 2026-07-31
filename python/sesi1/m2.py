#mencoba membuat program untuk main tebak angka
import random 

angka = random.randint(1,100)

while True:
    tebak = int(input("tebak angka yang akan keluar = "))

    if tebak == angka:
        print("kamu benarr ")
        break
    elif tebak >= angka:
        print("terlalu besar ")
    elif tebak <= angka:
        print("terlalu kecil")
