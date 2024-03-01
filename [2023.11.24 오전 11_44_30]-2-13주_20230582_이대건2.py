balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
print(balls[4])

for item in balls:
    print('item :',item)
print('--------------------')

for index, item in enumerate(balls):
    print('index : ',index,', item :',item)
print('--------------------')
i = 0

while i < len(balls):
    print(balls[i])
    i += 1
print('--------------------')

print(balls[len(balls)-1])

print(balls.index('탁구공'))
print('--------------------')

str = 'tpython'
print(str.index('th'))

balls.append('테니스공')
print(balls)