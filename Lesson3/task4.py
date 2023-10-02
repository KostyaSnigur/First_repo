def discount_price(price, discount):
    def apply_discount():
       nonlocal price
       price = price - (price * discount)
    apply_discount()
    return price
result = discount_price(100, 0.1)
print(result)