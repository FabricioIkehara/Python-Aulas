n1 = input("Digite sua nota da n1:")
n2 = input("Digite nota da n2:")

n1 = eval(n1)
n2 = eval(n2)

media = 0.4 * n1 + 0.6 * n2

if media >= 5:
    print("Você foi aprovado!!")
else:
    print("Você foi reprovado, burro!")