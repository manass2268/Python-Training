# ================================

# Random module
"""
import random as r

#This Function nly return the float value within 0 to 1
print(r.random())
"""

# ========================
"""import unifrom as r


#uniform this returns random floating-point number in the range [a, b)
a=10 
b=40
print(r.uniform(a, b))
"""
# -=========================

"""import random as r

# Randint is the strting or ending value between them
a = 10
b = 40
#print(r.uniform(a, b))

print(r.randint(1000, 9999))"""

"""import random as r

# Randint is the strting or ending value between them
a = 10
b = 40
# print(r.uniform(a, b))

print(r.randrange(1, 50))
"""
# ==============
# This Method return a randomly slecetd value from specified range
"""import random as r

# Randint is the strting or ending value between them

print(r.randrange(1, 50))
"""
# =======================
"""import random as r

# Randrange value pass within the step value alsoo 
print(r.randrange(1, 50, 2))
"""
# ================
# Choicee method retruns the slected method of the list

import random as r

Alpha = ["A", "B", "C", "D"]

print(r.choice(Alpha))
