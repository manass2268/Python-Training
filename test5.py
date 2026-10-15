#l=[100,200,300,400,500]
'''print(l,type(l)) #[100, 200, 300, 400, 600] <class 'list'>
print(l[0]) # 100
print(l[-1]) #b 600
print(l[0:3])  #[100, 200, 300]
print(l[::-1])  #[600, 400, 300, 200, 100]
print(l[-2:-5:-1]) # [400, 300]

print(len(l))
print(max(l))
print(min(l))
print(sum(l))'''

'''l.append(600)
print(l)'''

#========================================================
'''name=[]
for i in range(5):
    n= input(f"Enter the Name of {i+1} Friend: ")
    name.append(n)

print(name)'''

#==================================================
#l=[100,200,300,400,500]
'''l2=l.copy()
l2 =l

print(l)
print(l2)

l.append(600)
print(l)
print(l2)'''


'''l.append([600,700,800])
l.extend([600,700,800])
print(l)'''

'''print (400 in l)
print(l.index(4001))
print(l.insert(2,0))'''

'''print(l.pop())
print(l.pop(3))
print(l.remove(300)) #must [pass the one value]
'''
#del l[2:]

'''print(l.clear())
print(l.reverse())

print(l)'''

#======================
'''l=[45,89,478,157,145,516,518,218,2180,51484,7851]
l.sort()
print(l)#[45, 89, 145, 157, 218, 478, 516, 518, 2180, 7851, 51484]


l.sort(reverse=True)
print(l) #[51484, 7851, 2180, 518, 516, 478, 218, 157, 145, 89, 45]
'''


#friendsName=["Sachin","Virat","Annop","Yuvi"]
'''def myfun(ele):
    return ele[1]

#  friendsName.sort(key=len)
friendsName.sort(key=myfun)
print(friendsName)'''

#============================
l1=[1,2,3,"MANAS","RAM",[1,2,3],5.67]
l2=[4,5,6,7]

'''print(l1+l2) #[1, 2, 3, 4, 5, 6, 7]
print(l1+5) #Eroror
print(l1*l2) #Error
print(l1 *3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]
print(l1/l2) #Error
print(2 in l1) #True'''

