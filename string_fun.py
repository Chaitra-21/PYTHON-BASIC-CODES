print("hello".count("e"))
test="happy birthday"
print(test.count("a"))
print(test.count("day"))
print("-----------------------------------------------------------------------")
x="Independence Day"
print(x.lower())
print(x.upper())
print(x)
x=x.upper()
print(x)
x=x.lower()
print("----------------------------------------------------------------------------")
z="womens day"
print(z)
print(z.capitalize())
print(z.title())
print(x.isupper())
print(z.istitle())
print("----------------------------------------------------------------------------")
a="AmazonSale"
print(a.isalpha())      #checks if string conttains only letter, if space is encountered then it returns false
a="12345"
print(a.isdigit())
a="happy123"
print(a.isalnum())
a="happy@123"
print(a.isalnum())
print("---------------------------------------------------------------------------")
u="cool cabs"
print(u.index("cabs"))
print(u.find("ool"))
print("----------------------------------------------------------------------------")
k="0000000000happysoul000000000"
print(k.strip("0"))
print(len(k))

