first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = ""
if first < second:
    gcd = first
    print(gcd)
elif second < first:
    gcd = second
    print(gcd)
else:
    gcd = "equal"
    print(gcd)

while (first % gcd != 0) or (second % gcd != 0):
    gcd = gcd - 1
print(gcd)