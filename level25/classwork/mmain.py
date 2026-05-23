def check_ticket_price(age):
    if age < 12:
        return "ბილეთი არი უფასო შენთვის"
    elif age <= 18:
        return "ბილეთის ფასი არი 10 ლარი შენთვის"
    else:
        return "ბილეთის ფასი არი 20 ლარი შენთვის"


print(check_ticket_price(10))
print(check_ticket_price(15))
print(check_ticket_price(25))
