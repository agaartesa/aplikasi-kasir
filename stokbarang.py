#data barang dan stok
barang = ["Buku","Pensil","Penghapus","Penggaris","Spidol"]
stok = [10, 0, 5, 3, 0]

#meminta input
nama_barang = input("Masukkan nama barang: ")

#indexing
indeks = 0
ketemu = False

while indeks < len(barang):
    if barang[indeks].lower() == nama_barang.lower():
        ketemu = True
        if stok[indeks] > 0:
            print (f"Barang: {barang[indeks]} - Tersedia (Stok: {stok[indeks]})")
        else:
            print (f"Barang: {barang[indeks]} - Habis (Stok: {stok[indeks]})")
        break
    indeks +=1
if not ketemu:
    print("Barang Tidak Ditemukan!!!")

#latihan : coba modifikasi program dengan user bisa menambah
#dan mengurangi barang & stok barang
      