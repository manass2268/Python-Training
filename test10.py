# ===================================List Comprehension=======================================

"""
l=list(range(1,51))

nL=[]
"""

"""
Parameter --> 
1. Expression

"""
# userName=['Amit',]

# Nested List
"""
Nested List Comprehensions are nothing but a list comprheension within another list comprehension white is quite simplar to nested for loop
"""

"""
#1 Dimension
mat=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for row in mat for num in row]
print(flat)
#2-Dimension

# mat=[[1,2],[4,5],[7,9]] 
flat=[[j for j in range(5)] for i in range(3)]
print(flat)"""

"""
# if else or for loop with range and list compherenstion

#l=["Even number" if i%2==0 else "Odd Number" for i in range(10)]

#l=["Even number "+str(i) if i%2==0 else "Odd Number "+str(i) for i in range(10)]
l=[f"Even number {i}" if i%2==0 else f"Odd Number {i}" for i in range(10)]
print(l)
"""

# ===================================Dictionary Comprehension=======================================

"""
#s={ele:ele**2 for ele in range(10)}
s={f"Key{ele}":ele**2 for ele in range(10)}
print(s)
"""
Pr = {}
