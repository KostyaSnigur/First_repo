age = int(input("age >>>"))
hour = int(input("what's an hour >>>"))
have_id = bool(int(input("do you have id card(1 - yes? 0 - no) >>>")))

condition = (age >= 18 and have_id) or hour == 22

if condition:
    print("You can by alcohol")
elif age == 18:
    print("Congrats! You can buy first beer in your life")
else:
    print("Tou are too young")    