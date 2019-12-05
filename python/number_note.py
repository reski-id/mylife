
# Penjumlahan
2+1

# Pengurangan
2-1

# Perkalian
2*2

# Pembagian
3/2

# Powers
2**3

# Can also do roots this way
4**0.5

# Order of Operations followed in Python
2 + 10 * 10 + 3

# Can use parenthesis to specify orders
(2+10) * (10+3)


## Variable Assignments

# Let's create an object called "a" and assign it the number 5
a = 5

# Adding the objects
a+a


# Reassignment
a = 10

# Check
a


# Yes! Python allows you to write over assigned variable names. We can also use
# the variables themselves when doing the reassignment. Here is an example of what I mean:

# Check
a

# Use A to redefine A
a = a + a

# Check
a


# The names you use when creating these labels need to follow a few rules:
#
#     1. Names can not start with a number.
#     2. There can be no spaces in the name, use _ instead.
#     3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#     3. It's considered best practice (PEP8) that the names are lowercase.
#


# inisiasi
penghasilan = 6000000

tax_rate = 0.1

pajak = penghasilan*tax_rate

# tampilkan Pajak !
print("penghasilan {} dan Tax Rate {}".format(penghasilan,tax_rate))
print("Pajak :>",penghasilan-pajak)

