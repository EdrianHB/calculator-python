#Faça um programa que simule uma calculadora, o programa deverá perguntar qual a operação que o usuário deverá realizar e 
# em seguida perguntar os valores da operação. As operações devem estar guardadas em funções num módulo

import ep10

print("Escolha uma operação a ser realizada:")
print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
op = int(input("Número da operação desejada: "))

print("")
n1 = int(input("Escolha o 1º número: "))
n2 = int(input("Escolha o 2º número: "))

if op==1:
    a = ep10.som(n1,n2)
    print(f"A soma é {a}.")
elif op==2:
    s = ep10.sub(n1,n2)
    print(f"A subtração é {s}.")
elif op==3:
    m = ep10.mul(n1,n2)
    print(f"O produto é {m}.")
elif op==4:
    d = ep10.div(n1,n2)
    print(f"A Razão é {d}.")
