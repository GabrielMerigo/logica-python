'''
# 1 - Ler dois números e imprimir as variáveis na mesma ordem que foram digitadas:
numero1 = input('Numero 1: ')
numero2 = input('Numero 2: ')
print('Numero 1 é: ' + numero1 + 'Número 2 é: ' + numero2)
'''

'''
# 2 -
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
# 3 - 
num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))
soma = num1 + num2
print('a soma desses números é: ', soma)
'''

'''
# 4 - 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
result = (num1 + num2 + num3) / 3
print('a média aritmética dos 3 valores é: ', result)
'''

'''
# 5 - 
numeros = [10, 10, 20, 15, 20]
numerosLength = len(numeros)
soma = 0
for i in range(numerosLength):
    soma = soma + numeros[i]
media = soma / 5
print(f"Soma={soma} Media={media}")
'''

'''
# 6 - 
num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))
if(num1 > num2):
    print('O primeiro número é maior que o segundo')
elif (num2 > num1):
    print('O segundo número é maior que o primeiro')
else:
    print('Os dois são iguais.')
'''
'''
# 7 -
arr = [2, 65, 3, 90, 80, 24]
print(arr)
arr.sort()
print(arr)
'''

'''
# 8 -
a = 100
b = 10
c = 2
soma = (a - b) * c
print(soma)
'''

'''
# 9 -
x = 10
y = 3
z = 10
soma = (( x - 5) * y) - z
print(soma)
'''

'''
# 10 - 
peso1 = 5
peso2 = 7
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

somaPesos = peso1 + peso2
media = ((nota1 * peso1) + (nota2 * peso2)) / somaPesos
print('Media ponderada', media)
'''

'''
# 11 -
fahrenheit = 54
soma = ((fahrenheit - 32) * 5) / 2
print(soma)
'''
'''
# 12 -
distancia = int(input('Distância em KM: '))
kmPorLitro = float(input('Quantos km por litro: '))
preco = float(input('Qual é o preço da gasolina: '))

def calculaLitros(distancia, kmPorLitro):
    return int(distancia / kmPorLitro)
    
litros = calculaLitros(distancia, kmPorLitro)
precoGasto = litros * preco
message = f"Com a quantidade de {str(distancia)} percorrida você irá gastar {str(litros)} litros de gasolina e terá que pagar {str(precoGasto)} reais."

print(message)
'''

'''
# 13 - 
num1 = int(input('Digite um número: '))

if(num1 <= 10):
    print('O seu número é menor que 10 ou igual a 10')
elif (num1 > 10 and num1 <= 100):
    print('O seu número é maior que 10 e menor que 100')
else:
    print('O seu número é maior que 100')
'''

'''
Faça um algoritmo que leia, para 8 pessoas, seus nomes e idades. 
Após, mostre o nome e a idade da pessoa mais nova.
'''


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

newestPerson = Person('', 2000)
vzs = ''

while vzs != 'N':
    currentPerson = Person(input('Digite o nome da pessoa: '), int(input('Digite a idade da pessoa: ')))

    if(currentPerson.age < newestPerson.age):
        newValuePerson = currentPerson
    else:
        newValuePerson = newestPerson
    vzs = input('quer continuar? caso sim [Digite Y] - caso não [ Digite N] ')

print(f"a pessoa mais nova é o(a) {newValuePerson.name} com a idade de {newValuePerson.age} anos")
