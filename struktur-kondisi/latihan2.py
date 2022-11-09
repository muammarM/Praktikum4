# variable angka untuk menampung jumlah angka yang diinputkan berupa array/list
angka = []
# variable bilangan untuk menentukan jumlah bilangan yang diinginkan
bilangan = input("Masukan jumlah bilangan yang diinginkan : ")

# Mengkonversi input string ke integer karena method input() selalu mengambil type dara string
bilangan = int(bilangan)

print("Program mengurut data")

# melakukan perulangan berdasarkan jumlah dari variable bilangan

for i in range(0, bilangan):
    # melakukan perulangan input sampai jumlah dari variable bilangan yang sudah ditentukan
    # misal bilangannya sama dengan 4 maka akan dimunculkan input 4 lalu disimpan divariable => data

    data =  int(input("Masukan bilangan ke-" + str(i=1) + " : "))

    # menambahkan isi dari variable data ke variable angka yang type datanya berupa array
    # contoh input pertama [3] => input ke-dua [3,5] => input ke-tiga [3,5,2] => input ke-empat [3,5,2,9] dan seterusnya sesuai jumlah variable bilangan
    angka.append(data)

# menampilkan hasil program
# method sorted() berfungsi untuk mengurutkan nilai dari terkecil ke terbesar,
print("Bilangan yaang sudah diurutkan  dari terkecil ke terbesar", sorted(angka))