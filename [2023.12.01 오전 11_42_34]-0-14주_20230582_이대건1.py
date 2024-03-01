#append와 insert 함수에 대해 복습하기
sports = ['농구', '축구', '야구', '배구']

#append는 뒤에 추가하는 함수
print(sports)

sports.append('농구')
print(sports)
#출력되면 축구 야구 배구 농구

list1 = [1,2,3]
list2 = [10,20,30]
list3 = [100,200,300]

print(list1)
print(list2)
print(list3)

list1.extend(list2) 
#list1에 list2가 추가됨
print(list1)

list2 = list2 + list3
#'+'기호로 리스트를 합칠 때는 어디에 저장되는지 정할 수 있다
print(list2)

print(sports)
#리스트의 마지막 아이템 삭제
#pop은 삭제된 값을 반환해서 가지고 있음
print(sports.pop(2))
print(sports)

del sports[1]
print(sports)

sports.remove('농구')
#'농구'의 인덱스 번호도 모르겠고 그냥 아이템을 지우고 싶을 때
print(sports)

#만약 농구가 여러개일때 remove하면? --> 같은 데이터가 여러개일때는 앞에있는거 하나만 지운다