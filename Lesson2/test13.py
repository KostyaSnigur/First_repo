message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    pos = ord("r") - ord("c") 
    pos = (pos + 28) % 26 
    new_char = chr(pos + ord("r")) 
    print(new_char)
