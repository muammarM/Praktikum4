# menerima input yang diketik dan menyimpan didalam variable
bilanganSatu = input("Masukan bilangan pertama : ")
bilanganKedua = input("Masukan bilangan kedua : ")

# mengkonversi input String ke integer karena method input() selalu mengambil type data string
bilanganSatu = int(bilanganSatu)
bilanganKedua = int(bilanganKedua)

# mengecek untuk menentukan bilangan terbesar dari kedua bilangan
if bilanganSatu > bilanganKedua:
    print("Bilangan", bilanganSatu, "lebih besar dari bilangan", bilanganKedua)
else:
    print("bilangan ", bilanganKedua, "lebih besar dari bilangan", bilanganSatu)