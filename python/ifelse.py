age = 55

name = "Dr Grigory House"

#jika umur lebih dari 18 bisa mendapatkan licence

if(age>=18):
    print ("lebih dari 18 tahun")
    print ("Kamu bisa mendapatkan Licence")
else:
    print ("umur anda")
    print ("Kamu belum bisa mendapatkan Licence")

if(name=="Dr Grigory House"):
    print ("Hai Doctor")
else:
    print ("Hello ?")

#jika cuaca cerah => ayo main
cuacacerah= False
if(cuacacerah):
    print ("let's go main")
else:
     print ("Cuaca tidak cerah")

#jika bilangan lebih besar atau kecil dari 4
x=5
if x<4:
    print ("kecil dari 4")
else:
    print ("besar dari 4")

#tentukan bilangan ganjil dan genap
angka = int(input("Masukkan Angka :"))
if angka % 2 is 0:
    print("Bilangan Genap")
else:
    print("Bilangan Ganjil")
