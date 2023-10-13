payments = [300, 453, -43, 101]

def amount_payment(payments):
    total = 0
    for payment in payments:
        if payment > 0:
            total += payment
    return total
res = amount_payment(payments)
print(res)
        