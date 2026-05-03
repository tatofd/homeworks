password = "1234"

user_input = input("შეიყვანე პაროლი: ")

while user_input != password:
    print("არასწორია, თავიდან სცადე!")
    user_input = input("შეიყვანე პაროლი: ")

print("პაროლი სწორია !!!!!!!!!!!!!")