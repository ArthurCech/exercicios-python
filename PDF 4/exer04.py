print('Exercício 04 do PDF Parte 4')

fileAnswer = open('exer04.txt', 'w')

qtd = 0
while qtd <= 0:
    qtd = int(input('Digite a quantidade de elementos: '))

num = 0
while num <= 0:
    num = float(input('Digite um número real: '))
    if num > 0:
        maior = menor = num
i = 0
while i < qtd - 1:
    num = float(input('Digite um número real: '))
    if num <= 0:
        print('número inválido')
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        i += 1

print('Menor valor = {}'.format(menor))
print('Maior valor = {}'.format(maior))
print('Menor valor = {}'.format(menor), file=fileAnswer)
print('Maior valor = {}'.format(maior), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')