message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if "a" <= ch <= "z":
        pos = (ord(ch) - ord('a') + offset) % 26
        new_ch = chr(pos + ord('a'))
        encoded_message = new_ch
    elif "A" <= ch <= "Z":
        pos = (ord(ch) - ord('A') + offset) % 26
        new_ch = chr(pos + ord('A'))
        encoded_message = new_ch