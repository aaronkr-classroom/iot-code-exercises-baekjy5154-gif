-다음 내용을 하나의 조건식으로 만드세요.
홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
8월 15일이면 "광복절"을 출력함.
그 외는 "평일"을 출력함.
변수는 month와 day를 사용함.

result = "광복절" if (month == 8 and day == 15) else ("그날" if ((month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16)) else "평일")
 month == 8 and day == 15 → 광복절 우선 처리
(month % 2 == 1 and day == 15) → 홀수 달 15일
(month % 2 == 0 and day == 16) → 짝수 달 16일
그 외 → "평일"



-for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요. 
total = 0

for i in range(1, 51):
    if i % 2 == 0 and i % 3 != 0:
        total += i

print(total)

i % 2 == 0 → 짝수만 선택
i % 3 != 0 → 3의 배수 제외
조건을 만족하는 값만 total에 누적합니다.




-연습문제 4.3을 while 문으로 해결하세요. 

i = 1
total = 0

while i <= 50:
    if i % 2 == 0 and i % 3 != 0:
        total += i
    i += 1

print(total)

while i <= 50 → 1부터 50까지 반복
i % 2 == 0 → 짝수
i % 3 != 0 → 3의 배수 제외
조건을 만족하면 total에 누적 후 출력합니다.
