menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

	opcao = input(menu)

	if opcao == "d":
		print("Dep�sito")

	elif opcao == "s":
		print("Saque")

	elif opcao == "e":
		print("Extrato")

	elif opcao == "q":
		break

	else:
		print("Opera��o inv�lida, por favor selecione novamente a opera��o desejada.")
