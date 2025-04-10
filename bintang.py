baris = int(input("Masukkan Jumlah Baris: "))

for i in range (1, baris + 1):
    for j in range(1, i + 1):
        print (j, end=" ")

#range (start, stop, step) 
#start = titik awal (opsional) / default nya 0
#stop = titik berhenti (tidak termasuk hasil)
#step = langkah-langkah (bisa +1 / -1) dsb 