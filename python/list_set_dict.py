animal=["Duck","Chicken","Dog","Cow","Rat","Rabbit","Horse"]

cartoon=["Spongebob","Rick and Morty","Jhonny English","Tom and Jerry"]

belanjaan = ["kopi","susu","rice","lipstick","Buku"]

print(belanjaan[::])

belanjaan.insert(5,"SoftDrink")
belanjaan.remove("Buku")

lst=[[1,2],[3,4]]
print(sum(lst,[]))

for x in belanjaan:
    print(x)

if "Buku" in belanjaan:
    print("Buku ada dalam Daftar list belanjaan")
else:
    print("Buku tidak ada dalam list")