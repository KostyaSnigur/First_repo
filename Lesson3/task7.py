def first(size, *arguments):
    return size + (len(arguments))
    
print(first(5, "first", "second", "third"))

def second(size, **key_arguments):
    return size + (len(key_arguments))

print(second(3, comment_one="first", comment_two="second", comment_third="third"))
