# ===========================1=======================
"""prDetails=[
    {"proId":101,"proName":"Hero","proPrice":20},
    {"proId":102,"proName":"Master","proPrice":40},
    {"proId":103,"proName":"Cobeter","proPrice":30},
    {"proId":104,"proName":"System","proPrice":45},
    {"proId":105,"proName":"Refelex","proPrice":80},
    {"proId":106,"proName":"Supper","proPrice":70}

]

keys= prDetails[0].keys()
for key in keys:
    print(str(key).center(20),end=" ")

for product in prDetails:
    print()
    values=product.values()
    for value in values:
        print(str(value).center(20),end=" ")"""

# ==================================2
prDetails = [
    {"proId": 101, "proName": "Hero", "proPrice": 20},
    {"proId": 102, "proName": "Master", "proPrice": 40},
    {"proId": 103, "proName": "Cobeter", "proPrice": 30},
    {"proId": 104, "proName": "System", "proPrice": 20},
    {"proId": 105, "proName": "Refelex", "proPrice": 80},
    {"proId": 106, "proName": "Supper", "proPrice": 70},
]


def myfun(ele):
    return ele["proPrice"] == 20


# FilterPr=filter(myfun,prDetails)
FilterPr = filter(lambda ele: ele["proPrice"] == 20, prDetails)
print(list(FilterPr))
