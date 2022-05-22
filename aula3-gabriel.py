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

linhas = int(input('Quantas linhas?'))
colunas = int(input('Quantas colunas?'))

for i in range(linhas):
    if(i == 0 or i == linhas - 1):
        print('#'*(colunas + 2))
    else:
        print('#' + "."*colunas + '#')
'''
frase = input('Digite uma frase: ')
countVogal = 0

def isVogal(vogal):
    vogais = ['a', 'e', 'i', 'o', 'u']
    return vogal in vogais

for caractere in frase:
    caractereLower = caractere.lower()

    if(isVogal(caractereLower)):
        countVogal = countVogal + 1
        
print(f"A quantidade de caracteres da sua frase é {len(frase)}. E a quantidade de vogais é {countVogal}")

'''
Faça um algoritmo que leia vários números e identifique se o número é par, impar ou negativo.
Se for par adicione em uma lista chamada lista_pares, se for impar, adicione em lista_impares e 
se for negativo adicione na litsa chamada lista_negativos
'''


lista_pares = []
lista_impares = []
lista_negativos = []

while True:
    print("Digite 'sair' para finalizar...")
    numero = input('>>> ')
    if numero == "sair" : break

    try:
        numero = int(input('>>> '))
    except:
        print('Ops... você digitou algo que não é um número...')
        continue

    if numero >= 0:
        if numero % 2 == 0:
           lista_pares.append(numero)  
        else:
           lista_impares.append(numero)  
    else: 
       lista_negativos.append(numero) 

print(lista_pares, lista_impares, lista_negativos)

'''
import numpy as np 

primeira_faixa = []
segunda_faixa = []
terceira_faixa = []

'''ROTINAS'''
def criar_mensagem(nomeFaixa, qntdIdadesNaFaixa):
    if qntdIdadesNaFaixa.__len__() == 0:
        mensagem = f'{nomeFaixa} não houve alunos digitados \n'
    else:
        mensagem = f'{nomeFaixa} é {max(qntdIdadesNaFaixa)} anos \n'
    return mensagem
    
def verificarMediaTurma(media):
    if media <= 25 : return 'Jovem'
    if media >= 26 and media <= 60 : return 'Adulta'
    if media >= 61 : return 'Idosa'

def calculaMediaERetornaMensagem(qntdAlunos): 
    media = sum(qntdAlunos) / int(qntdAlunos.__len__())

    print(
        f'- A média de idades da Turma é: {media}\n',
        f'- Portanto, pode-se dizer que a turma é {verificarMediaTurma(media)}\n', 
        'Para essa turma a maior idade digitada para a: \n',
        criar_mensagem('primeira faixa', primeira_faixa),
        criar_mensagem('segunda faixa', segunda_faixa),
        criar_mensagem('terceira faixa', terceira_faixa)
    )

def concatArrays():
    return np.concatenate((primeira_faixa, segunda_faixa, terceira_faixa))

'''Lógica para criação do algoritmo'''
while concatArrays().__len__() <= 41:
    valorDigitado = input('Digite a idade do aluno ou digite "fim" para sair: ')
    qntdAlunos = concatArrays()

    if str(valorDigitado).lower() == 'fim':
        if qntdAlunos.__len__() == 0: 
            print('Você finalizou o processo sem digitar nenhuma idade...') 
            break
        calculaMediaERetornaMensagem(qntdAlunos)
        break

    try:
        idade = int(valorDigitado)
    except:
        print('Ops... algo aconteceu de errado! Verifique se você realmente está digitando número.')
        continue
    
    if idade >= 0 and idade <= 25:
        primeira_faixa.append(idade)
    elif idade >= 26 and idade <= 60:
        segunda_faixa.append(idade)
    else:
        terceira_faixa.append(idade)

calculaMediaERetornaMensagem(qntdAlunos)

 
