height = int(input('어린이의 신장을 입력하세요: '))
str = '탑승가능' if height >= 120 and height < 170 else '탑승 불가능'
print(str)
