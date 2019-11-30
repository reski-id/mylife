# Mengambil data nama dan umur dari user dan menampilkannya di console
print("Masukkan Nama dan Umur")
print(10*"-")

name = input("Masukkan Nama :")
age = input("Masukkan Umur :")

print("hello  {} umur anda adalah {} Tahun".format(name,age))


# Mengambil data nnominal bayar dan harga barang  dari user dan menampilkannya dalam bentuk sisa bayar di console
print("Masukkan nominal harga dan Jumlah Bayar")
print(20*"-")
nominal = int(input("Masukkan nominal harga:"))
bayar = int(input("Masukkan Jumlah Bayar :"))

sisa = (nominal-bayar)

print("Sisa =",sisa)

# satu baris komentar dalam python

"""beberapa 
baris 
komentar"""