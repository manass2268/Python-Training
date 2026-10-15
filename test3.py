#Decorators
'''def myfun():
    print("fun calling")
def OutterFun(fn):
    def innerFun():
        print("Welcome user")
        fn()
        print("Thanks for using my function")
    return innerFun

a=OutterFun(myfun)
a()
myfun()'''

'''def OutterFun(fn):
    def innerFun():
        print("Welcome user")
        fn()
        print("Thanks for using my function")
    return innerFun
#OuterFunction
@OutterFun
def myfun():
    print("fun calling")


myfun()'''


'''def mydivd(a,b):
    return a/b

res= mydivd(5,10)
print("Result:",res)

res= mydivd(101,542)
print("Result:",res)
res= mydivd(421,985)
print("Result:",res)
res= mydivd(140,0)
print("Result:",res)
res= mydivd(610,989)
print("Result:",res)

'''

'''def decoratrorFun(fn):
    def innerFun(a, b):
        if b!=0:
            return fn(a,b)
        else:
            return "Division by zero is not allowed"
    return innerFun

@decoratrorFun

def mydivd(a,b):
    return a/b

res= mydivd(5,10)
print("Result:",res)

res= mydivd(101,542)
print("Result:",res)
res= mydivd(421,985)
print("Result:",res)
res= mydivd(140,0)
print("Result:",res)
res= mydivd(610,989)
print("Result:",res)'''

import time
def decoratorFun(fun):
    def innerFun():
        start_time = time.time()
        end_time = time.time()
        print(f"Function executed in {end_time - start_time} seconds")
    return innerFun

@decoratorFun
def myfun():
    print("Function Calling")

@decoratorFun
def happy():
    for i in range(1000000):
        pass
    
@decoratorFun
def sad():
    sum = 0
    for i in range(10000000):
        sum=sum+i
    print("Sum:",sum)

myfun()
happy()
sad()