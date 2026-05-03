# for როცა წინასწარ ვიცით რამდენჯერ უნდა შესრულდეს
# while მუშაობს მანამდე, სანამ პირობა არის ჭეშამრიტი
password = "1234"
user_input = input("Entერ password: ")

while user_input != password:
    user_input = input("Wrong password, try again: ")

print("Access granted")

# --
i = 1

while i <= 10:
    print(i)
    i += 1
    # --
    i = 2

while i <= 20:
    print(i)
    i += 2
    