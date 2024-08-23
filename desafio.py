#Entre com o nome do usuário
user = input("Digite seu nome:")
#Entre com o salário do usuário
salario = float(input("Digite seu salário:"))
#Entre com o bonus do usuário
bonus_user = float(input("Digite sue bônus:"))
#Variável que será alterado anualmente
percent = 1000
#Cálculo do KPI final
bonus_final = percent + salario*bonus_user
#Mensagem final
print(f"Olá {user}, o seu bônus foi de {bonus_final}.")
