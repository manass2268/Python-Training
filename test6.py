#===========Tuple=========================
'''t=(1,2,3,4,5)
print(t[1])#2
#t[2]=100 #Errorr

for ele in t:
    print(ele)
    
    
print(len(t))
print(max(t))
print(min(t))
print(sum(t))'''


#/////////////////////////////
'''x,y=10,20
print(x,y)

x,y=y,x     #Swapping                                            
print(x,y)
'''
'''
t=(3,1,7,8,1,8,3,7,9,9,3.6,6,3,3,7,3,4,9,7,5)
s=sorted(t) #sorted in the list
print(s) #[1, 1, 3, 3, 3, 3, 3, 3.6, 4, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9]

s=tuple(sorted(t))  #sorted in the tuple 
print(s)#(1, 1, 3, 3, 3, 3, 3, 3.6, 4, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9)
'''

#=====================================================================
'''t=("Manas","Shalini","Rohan","Aman","Shivam","Raj")
s=sorted(t)
print(s) #['Aman', 'Manas', 'Raj', 'Rohan', 'Shalini', 'Shivam']

s=sorted(t,key=len)
print(s) #['Raj', 'Aman', 'Manas', 'Rohan', 'Shivam', 'Shalini']

def my(ele):
    return ele[-1]
s=sorted(t,key=len)
print(s) #['Raj', 'Aman', 'Manas', 'Rohan', 'Shivam', 'Shalini']

s=sorted(t,key=len,reverse=True)
print(s) #['Shalini', 'Shivam', 'Manas', 'Rohan', 'Aman', 'Raj']
'''

#========================================
'''l = list(range(1,21))
print(l) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

NList= []
for ele in l:
    if ele%2==0:
        NList.append(ele)

print(NList)#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
     '''   
'''

# Filter Functiom
l= [5,2,6,7]
def myFun(ele):
    if ele%2==0:
        return True

NList= list(filter(myFun,l))
print(NList) #[2, 6]
'''
'''
l= [5,2,6,7]
def myFun(ele):
    if ele%2==0:
        return True

#NList= list(filter(myFun,l))
NList= list(filter(lambda))
print(NList)
'''

#==========================================
'''l=[1,2,3,4,5]
def myfun(lst):
    return lst**3
NList =list(map(myfun,l))
print(NList) #[1, 8, 27, 64, 125]
'''

l = [1, 2, 3, 4, 5]
NList = list(map(lambda x: x**3, l))
print(NList)    
