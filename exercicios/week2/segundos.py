
conversao = (86400, 3600, 60, 1) 
entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = (entrada % conversao[0])
minutos = (horas % conversao[1])
segundos = (minutos % conversao[2])

dias = entrada // conversao[0]
horas = horas // conversao[1]
minutos = minutos // conversao[2]
segundos = segundos // conversao[3]

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))
