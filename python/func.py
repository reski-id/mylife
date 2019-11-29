#print name and age from user
name = input("your name is : ")
age = input("your age is : ")


def hello(name, age):
    return "hello {} you are {} years old\nHave a Great Day".format(name,age)

print(hello(name,age))