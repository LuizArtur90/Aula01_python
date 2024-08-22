user = input("Digite seu nome:")
salario = float(input("Digite seu salário:"))
bonus_user = float(input("Digite sue bônus:"))
percent = 1000

bonus_final = percent + salario*bonus_user

print(f"Olá {user},o seu bônus foi de {bonus_final}.")