
def cost_delivery(quantity, *goods, discount=0):
    price1 = 5
    price2 = 2
    res = price1 + (quantity - 1) * price2
    res = res - (res * discount)
    return res
   
cost_delivery(2, 1, 2, 3, discount=0.5)