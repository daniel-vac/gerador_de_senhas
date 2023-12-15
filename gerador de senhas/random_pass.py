import random

lis_num = []
lis_mai = []
lis_min = []
lis_car = []

for i in range(3):
    num_ale = random.randrange(9)
    lis_num.append(num_ale)
    let_mai = chr(random.randint(65, 90))
    lis_mai.append(let_mai)
    let_min = chr(random.randint(97, 122))
    lis_min.append(let_min)
    car_esp = chr(random.randint(33, 38))
    lis_car.append(car_esp)

random.shuffle(lis_num)
lis_num = str(lis_num)[1:-1]
lis_num = lis_num.replace(',', '')

random.shuffle(lis_mai)
lis_mai = str(lis_mai)[1:-1]
lis_mai = lis_mai.replace(',', '')

random.shuffle(lis_min)
lis_min = str(lis_min)[1:-1]
lis_min = lis_min.replace(',', '')

random.shuffle(lis_car)
lis_car = str(lis_car)[1:-1]
lis_car = lis_car.replace(',', '')

pas_fim = lis_mai + lis_min + lis_num + lis_car
pas_fim = str(pas_fim)[1:-1]
pas_fim = pas_fim.replace("'", "")
pas_fim = pas_fim.replace(' ', '')

print(pas_fim)