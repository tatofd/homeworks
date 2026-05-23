def calculate_budget(numbers):
    total = 0

    for i in numbers:
        total += i

    if total > 500:
        print("ხარჯები დიდია!")
    else:
        print("ბიუჯეტში ეტევით")


calculate_budget([100, 200, 300])