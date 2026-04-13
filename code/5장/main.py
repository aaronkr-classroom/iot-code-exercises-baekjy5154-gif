from SayDays import SayDays

while True:
    try:
        year = int(input("연도 입력: "))
        month = int(input("월 입력: "))
        day = int(input("일 입력: "))

        s = SayDays(year, month, day)

        print("올해 몇 번째 날:", s.days())
        print("남은 날짜:", s.days_left())
        print("요일(숫자):", s.weekday())
        print("요일(이름):", s.weekday_name())
        print("-" * 30)

    except:
        print("잘못된 입력입니다.")