#Currency exchange

a = int(input('What do you have in pesos? '))
b = int(input('What do you have in reais? '))
c = int(input('What do you have in soles? '))

a_exch_rate = .058
b_exch_rate = .2
c_exch_rate = .27

pesos_to_usd = a * a_exch_rate
reais_to_usd = b * b_exch_rate
soles_to_usd = c * c_exch_rate

total_usd = pesos_to_usd + reais_to_usd + soles_to_usd
print(total_usd)