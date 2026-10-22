# ================================

# Random module
import random as r

"""

#This Function nly return the float value within 0 to 1
print(r.random())
"""

# ========================
"""


#uniform this returns random floating-point number in the range [a, b)
a=10 
b=40
print(r.uniform(a, b))
"""
# -=========================

"""

# Randint is the strting or ending value between them
a = 10
b = 40
#print(r.uniform(a, b))

print(r.randint(1000, 9999))"""

"""

# Randint is the strting or ending value between them
a = 10
b = 40
# print(r.uniform(a, b))

print(r.randrange(1, 50))
"""
# ==============
# This Method return a randomly slecetd value from specified range
"""

# Randint is the strting or ending value between them

print(r.randrange(1, 50))
"""
# =======================
"""

# Randrange value pass within the step value alsoo 
print(r.randrange(1, 50, 2))
"""
# ================
# Choicee method retruns the slected method of the specfic sequnece(string,range,list,tuple or any other kind)
"""


Alpha = ["A", "B", "C", "D"]

print(r.choice(Alpha))"""

# ==========
# Sapmle method return a list with a randomly selction of a specified number of items from a sequence

"""
Alpha = ["A", "B", "C", "D"]

print(r.sample(Alpha, k=2))
"""

# ==========
# Shuflee method takes a sequence of list and reoragninse the order of the items

Alpha = ["A", "B", "C", "D"]

print(Alpha)
r.shuffle(Alpha)
print(Alpha)
