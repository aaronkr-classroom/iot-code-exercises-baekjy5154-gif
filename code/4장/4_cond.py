# 4_conditionals.py
temp = 16
msg = ""

if temp < 0:
    msg = "cold"
elit temp < 10:
    msg = "Mild"
elit temp < 20:
    msg = "good"
elit temp < 30:
    msg = "Hot"
else:
    msg = "Hell"
    
print(msg)

# 변수 = 참값 if 조건식 else 거짓값 (삼항 조건문)
msg = "Let's play" if temp > 15 else "stay home"
print(msg)