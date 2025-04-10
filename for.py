bilangan = int(input("Masukkan Angka: "))

print (f"Tabel Perkalian Untuk Bilangan {bilangan}:")
for angka in range(0,11):
    hasil = bilangan * angka
    print(f"{bilangan} x {angka} = {hasil}")