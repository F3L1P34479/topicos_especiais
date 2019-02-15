# Criar uma lista vazia
lista = []
# Criar uma lista com tamanho 10
lista2 = [""]*10

# Adicionar um elemento na lista
lista.append(5)
lista.append(15)
lista.append(12)
lista.append(35)
lista.append(40)
lista.append(11)
lista.append(47)
lista.append(21)

# Alterar valor da lista
lista[3] = 44

print("Resultado da lista: ", lista)

# Calcular tamanho da lista
t = len(lista)
i = 0

while i < t:

    #print("Na posição ", i, " tem o valor ", lista[i])
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

    i += 1
print("\n=====================================================\n")

# Usando o for da maneira foreach
for x in lista:
    print("Valor da lista: ", x)

print("\n=====================================================\n")

# Uso do for normal
# len calcula o tamanho da lista e range cria uma sequência numérica
for i in range(len(lista)):
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

# Criação de funções
def dobro(num):
    d = num * 2
    print("O dobro de {} é {}.".format(num, d))
    return d, num, 99

a, b, c = dobro(5)
print("Os retornos são: {} e {} e {}.".format(a, b, c))
