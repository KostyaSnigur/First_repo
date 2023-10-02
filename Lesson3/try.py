def first(size, *position_argument):
    print(position_argument)

first(5, "first", "second", "third")
first(1, "Alex", "Boris")
    
def second(title, **key_argument):
    print(key_argument)

second("size", 3, comment_one="first", comment_two="second", comment_third="third")
second("size", 10, comment_one="Alex", comment_two="Boris")
    