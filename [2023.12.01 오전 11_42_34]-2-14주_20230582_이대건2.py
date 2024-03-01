languages = ['java','c/c++','c#','java','c#']
print(languages)

for str in languages:
    if str == 'java':
        languages.remove('java')
#for문을 이용해서 리스트에서 반복되는 java 다 지우기

print(languages)

while('c#' in languages):
    languages.remove('c#')
#while문을 이용해서 리스트에서 c#다 지우기

print(languages)

fruits = ['사과','망고','당근','수박','포도','참외','토마토']
print('fruits :', fruits)

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)

print('fruits :', fruits)