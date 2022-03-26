
'''
1 - Ler dois números e imprimir as variáveis na mesma ordem que foram digitadas:
numero1 = input('Numero 1: ')
numero2 = input('Numero 2: ')

print('Numero 1 é: ' + numero1 + 'Número 2 é: ' + numero2)
'''

'''
2 -
vA = input('Escreva o primeiro número: ')
print('O valor digitado foi: ' + vA)
vB = input('Escreva o segundo número: ')
print('O segundo número foi ' + vB)

vC = vA
vA = vB
vB = vC

print('vA agora é: ', vA, 'vB agora é: ', vB)
'''

'''
3 - 
num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))
soma = num1 + num2
print('a soma desses números é: ', soma)
'''

'''
4 - 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

result = (num1 + num2 + num3) / 3
print('a média aritmética dos 3 valores é: ', result)
'''

'''
5 - 
numeros = [10, 10, 20, 15, 20]
numerosLength = len(numeros)

soma = 0
for i in range(numerosLength):
    soma = soma + numeros[i]
print(soma)
'''

'''
6 - 
num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))

if(num1 > num2):
    print('O primeiro número é maior que o segundo')
else:
    print('O segundo número é maior que o primeiro')
'''


'''
7 -
arr = [2, 65, 3, 90, 80, 24]
print(arr)
arr.sort()
print(arr)
'''

'''
8 - 
a = 100
b = 10
c = 2

soma = (a - b) * c
print(soma)
'''

'''
9 -
x = 10
y = 3
z = 10
soma = (( x - 5) * y) - z

print(soma)
'''

'''
10 -
fahrenheit = 54
soma = ((fahrenheit - 32) * 5) / 2
print(soma)
'''

distancia = int(input('Distância em KM: '))
kmPorLitro = int(input('Quantos km por litro: '))
preco = float(input('Qual é o preço da gasolina: '))

def calculaLitros(distancia, kmPorLitro):
    return int(distancia / kmPorLitro)
    
litros = calculaLitros(distancia, kmPorLitro)
precoGasto = litros * preco
message = 'Com a quantidade de ' + str(distancia) + ' percorrida ' + 'você irá gastar ' + str(litros) + ' litros de gasolina e terá que pagar ' + str(precoGasto) + ' reais.'

print(message)




