# ==============================Pyhton Iterator=============
"""lst=[10,20,30]
i=iter(lst)
#exception Handling
while True:
    try:
        print(next(i))
    except StopIteration:
        print("Exception handlinng")
        break
"""

# =================Itreable=========
"""
An itreable in python is any obejct that can you can loop over(iterate though)-like in an for loop.
An iterable is a collection of element that can retrun an iterator 
ex. list,tuple,string,set, dictornary
"""

# ======================Generator=========================
"""
1. Python a Generator is a function   that reurns an iterator that produces a sequence of values when iterated over.
2. Generator are usefual when we want to produce a large  sequnce of value, but we don't want to store all of them in memory at once.
3. CREATE Python Generator: In Python, similar to define  a normal function, we can define a genrator function using the def keyword,but instead of the return statement, we use the yield statement to produce a value.
4. Yield keyword is used to produce a value from the generator
5. When a generator function is called, it returns a generator object, which can be iterated over using the next() function or a for loop.
6. When the generator function is called, it does not execute the function body immediately. Instead , it returns a generator object that can be used to iterate over the values produced by the function. 
"""
