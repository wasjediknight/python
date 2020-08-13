fatura = {}

fatura["nome"] = input("Digite o nome do cliente: ")
fatura["dia"] = input("Digite o dia de vencimento: ")
fatura["mes"] = input("Digite o mês de vencimento: ")
fatura["valor"] = input("Digite o valor da fatura: ")

msg = "Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada."

print(msg.format(fatura["nome"], fatura["dia"], fatura["mes"], fatura["valor"]))
