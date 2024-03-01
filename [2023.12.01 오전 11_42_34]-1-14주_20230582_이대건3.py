names = ['홍길동','김길동','이길동','박길동','정길동']
print(names)

names.sort()
print(names)

names.sort(reverse= True)
#리스트를 내림차순으로 정렬해준다
print(names)

names = ['홍길동','김길동','이길동','박길동','정길동']
#reverse함수와 .reverse를 헷갈리지 않을 것
print(names)

names.reverse()
print(names)

animals = ['호랑이','사자','곰','여우','늑대']
print(animals)

#슬라이싱 표기법 [a:b], 맨 앞 또는 맨 뒤는 생략표기가 가능하다
print(animals[1:4])
print(animals[:3])
print(animals[3:])

print(animals[len(animals)-2:])
#끝에 두개만 출력한다