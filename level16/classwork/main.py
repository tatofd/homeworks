score = int(input("შეიყვანე ქულა: "))

if 90 <= score <= 100:
    print("შესანიშნავი ქულაა")
elif 70 <= score < 90:
    print("კარგი ქულაა")
elif 60 <= score < 70:
    print("ნორმალური ქულაა")
else:
    print("ჩაიჭერი, წადი ისწავლე")