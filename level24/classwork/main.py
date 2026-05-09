def average(arr):
    total = 0
    for i in arr:
        total += i
    avg = total / len(arr)
    print(avg)

average([10, 20, 30, 40])