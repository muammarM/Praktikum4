# import module random untuk mengenerate angka acak 0.3222. . .dst
from random import random
# variable jumlaiNilai menampung input masukan lalu diconvert ke integer
jumlahNilai = int(input('masukan jumlah nilai yang ingin dicari ; '))
# variable nilaiRandom & kurangDariNolKomaLima berupa array/list untuk menyimpan data yang diperlukan nanti.
nilaiRandom = []
kurangDariNolKomaLima = []
# loopin data berdasarkan jumlahNilai,
for i in range(0, jumlahNilai):
    # variable n = menyimpan angka random contoh: 0.9905112793033766
    n = random()

    # menambahkan n ke variable nilaiRandom
    # fungsi append() untuk menambahkan data ke dalam variable yang type datanya berupa array/list
    nilaiRandom.append(n)
    # apakah n < dari 0.5 ? jika iya tampilkan lalu break dan mulai angka random selanjutnya
    while n < 0.5:
    
        # menambahkan n jika kurang dari 0.5  ke variable kurangDariNolKomaLima
        kurangDariNolKomaLima.append(n)

        # menampilkan output n
        print("data ke-", str(i+1), " => ", n)
        break
print()
# menampilkan outputkeseluruhan nilai random
print("Berikut keseluruhan nilai random dari total ", jumlahNilai, "yaitu ", nilaiRandom)
print()
# menampilkan output keseluruhan nilai n < 0.5
print("Berikut nilai yang kurang dari 0.5 berjumlah ", len(kurangDariNolKomaLima), "yaitu ", kurangDariNolKomaLima)

