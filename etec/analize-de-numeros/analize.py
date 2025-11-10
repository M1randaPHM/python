lista=[]
for i in range(15):
    numero = int(input("Digite um numero: "))
    while numero in lista:
        numero=int(input("Número repetido! Digite outro número: "))
    lista.append(numero)

#Deixar a lista em ordem crescente
lista.sort()

par, impar = 0, 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par += 1
    else:
        impar += 1


print("Números em ordem crescente:", lista)
print("Maior número: ", max(lista))
print("Menor número: ", min(lista))
print("Soma dos números", sum(lista))
print("Média da lista", sum(lista) / len(lista))
print("Quantidade de números pares: ", par)
print("Quantidade de números ímpares: ", impar)