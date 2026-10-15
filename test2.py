# 1)reuqired psotional arrgument
'''def SI(amnt,rate,time):
    print(f"Amount : Rupess {amnt} ")
    print(f"Rate : {rate} %")
    print(f"Time : {time} Year")

SI(12500,5,4)'''

# 2) Default Value Arrgument
'''def SI(amnt,rate,time=1):
    print(f"Amount : Rupess {amnt} ")
    print(f"Rate : {rate} %")
    print(f"Time : {time} Year")

SI(12500,5,4)'''

'''
def SI(amnt=1000,rate,time=1): # Always define deafult arrgument after the non arrgument
    print(f"Amount : Rupess {amnt} ")
    print(f"Rate : {rate} %")
    print(f"Time : {time} Year")

SI(12500,)'''

'''def SI(rate,amnt=1000,time=1): # Always define deafult arrgument after the non arrgument
    print(f"Amount : Rupess {amnt} ")
    print(f"Rate : {rate} %")
    print(f"Time : {time} Year")

SI(120)'''

#3) Using Argument Name to declare or over write the arrgument value
'''def SI(rate,amnt=1000,time=1): 
    print(f"Amount : Rupess {amnt} ")
    print(f"Rate : {rate} %")
    print(f"Time : {time} Year")

SI(5, time=3)
SI(amnt=50000,time=5,rate=40)'''

n=5
for i in range(n):
    print(" "*(n-i),"*"*i)
    print(" "*(n-i)," *"*i)
    print(" "*(n-i),chr(65+i)*i)