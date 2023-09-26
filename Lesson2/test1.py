num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    for j in range(num + 1):
        sum = sum + j
        print(f"{sum}")
        num = int(input("Enter the integer (0 to 100): "))
    
      
           