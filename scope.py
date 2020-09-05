#global scope
a=100
'''def f1():
    print(a)
def f2():
    print(a)
f1()
f2()'''
print("-------------------------------------------------------------")
#local scope
print(a)
def fun1():
    print(a+300)
def fun2():
    print(a/2)
fun1()
fun2()
print(a)
