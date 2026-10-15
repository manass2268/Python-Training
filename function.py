#variable length argument
'''def myfun(**a):
    print(a,type(a))
myfun(empid=1001,empName='Sachin',empSalary=5600.00)'''

'''def myfun():
    print("fun calling")

#fun calling
#myfun()
print(myfun) #<function myfun at 0x01570398>
a=myfun
print(a) #<function myfun at 0x01570398>
a() #fun calling
'''
'''def mysum(a,b):
    print("Sum :" ,(a+b))

def mydiff(a,b):
    print("Diference :" ,(a-b))
#Function calling with Call back   
def myfun(x,y,fn):
    fn(x,y)

myfun(20,10,mysum) #Sum : 30
myfun(200,100,mydiff) #Diference : -100
'''

'''def outerFun():
    msg='welcome'
    print("OUTEER FUNCTION  ")

    def innerfun(name):
        print("INNER FUNCTION")
        print(msg ,name)

    return innerfun

fn = outerFun()
fn('Raunak')
'''

