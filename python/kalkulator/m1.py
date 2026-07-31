#fungsi menghitung
def hitung_angka(a, b, angka):
    if angka == 1:
        return a + b
    elif angka == 2:
        return a - b 
    elif angka == 3:
        if b == 0:
            return None
        return a / b
    elif angka == 4:
        return a * b
    else:
        return None

#tampilan menu
def kalkulator(a, b, angka, hasil):
    print("=" * 38)

    if angka == 1:
        print(f"{a} + {b} = {hasil}")
    elif angka == 2:
        print(f"{a} - {b} = {hasil}")
    elif angka == 3:
        print(f"{a} % {b} = {hasil}")
    elif angka == 4:
        print(f"{a} x {b} = {hasil}")

    print("-" * 38)

#program utama
print("=" * 38)
print("\t kalkulator sederhana")
print("=" * 38)
print("1. ditambah")
print("2. dikurang")
print("3. dibagi")
print("4. dikali")

angka = int(input("pilih pilihan diatas "))

if angka == 5:
    print("sampai bertemu kembali") 

a = int(input("angka pertama = "))
b = int(input("angka kedua = "))

hasil = hitung_angka(a, b, angka)

kalkulator(a, b, angka, hasil)
