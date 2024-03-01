endBirthYear = int(input('출생 연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))
if age >= 65:
    print('언제든지 구매 가능하십니다.')
else:
    if endBirthYear == 1  or endBirthYear == 6:
        print('월요일에 구매 가능합니다.')
    elif endBirthYear == 2  or endBirthYear == 7:
        print('화요일에 구매 가능합니다.')
    elif endBirthYear == 3  or endBirthYear == 8:
        print('수요일에 구매 가능합니다.')
    elif endBirthYear == 4  or endBirthYear == 9:
        print('목요일에 구매 가능합니다.')
    elif endBirthYear == 5  or endBirthYear == 0:
        print('금요일에 구매 가능합니다.')
