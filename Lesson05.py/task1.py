def real_len(text):
    chars =  ["\n", "\f", "\r", "\t", "\v"]
    real = 0
    for char in text:
        if char not in chars:
            real += 1
    return real


    #result = text.split()
    #return (result)
real_len('Alex\nKdfe23\t\f\v.\r')
res = real_len
print(res)