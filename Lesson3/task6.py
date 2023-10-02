def format_string(string, length):
        if len(string) >= length:
           return string
        else:
            for i in range((length - len(string)) // 2):
                string = " " + string
            return string
res = format_string ("abaa", 15)
print(res)
