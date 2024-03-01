weight = float(input('몸무게(kg) : '))
height = float(input('신장(cm) : ')) / 100 
bmi = int(weight / (height ** 2))
print('BMI : ', bmi)
