listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
  ]
cariKota = input("Masukkan Kota yang Dicari: ")
# bermain index
i = 0
while i < len(listKota):
    if listKota[i].lower() == cariKota.lower():
        print ("Ketemu di index", i)
        break
    print("bukan", listKota[i] )
    i+=1