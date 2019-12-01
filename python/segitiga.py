string = ""
baris = 1

Sisi = int(input("Masukkan Jumlah angka Sisi  :"))

# Looping Baris
while baris <= Sisi:
	kolom = baris

	# # Looping Kolom
	while kolom > 0:
		string = string + " * "
		kolom = kolom - 1
		
	string = string + "\n"
	baris = baris + 1
print (string)