def hitung_diskon(harga, diskon):
    potongan = (harga*diskon) / 100
    harga_setelah_diskon = harga - potongan
    return harga_setelah_diskon

harga_awal = 10000
persen_diskon = 20

harga_akhir = hitung_diskon(harga_awal,persen_diskon)
print(f"Harga Setelah Diskon adalah Rp {harga_akhir}")
