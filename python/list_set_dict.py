animal=["Duck","Chicken","Dog","Cow","Rat","Rabbit","Horse"]

cartoon=["Spongebob","Rick and Morty","Jhonny English","Tom and Jerry"]

lt_belanjaan = ["kopi","susu","rice","lipstick","Buku"]

# add more to list
# insert
# del
# len
print(lt_belanjaan[::])

lt_belanjaan.insert(5,"SoftDrink")
lt_belanjaan.remove("Buku")

for x in lt_belanjaan:
    print(x)

if "Buku" in lt_belanjaan:
    print("Buku ada dalam Daftar list belanjaan")
else:
    print("Buku tidak ada dalam list")