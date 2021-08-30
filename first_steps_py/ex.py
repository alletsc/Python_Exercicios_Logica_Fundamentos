#Exemplos
'''valores = list()
for cont in range (0,5):
    valores.append(int(input("Digite um valor: ")))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista')
'''
####
'''listA = [2,3,4,7]
listB = listA
print(listA)
print(listB)
print(listA[0])'''
####
'''pessoas = (['Pedro', 25], ['Ana', 36], ['Joao',78])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''
####
'''teste = list()
teste.append('Stella')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Josi'
teste[1] = 23
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 25],['Ana', 34],['Stella', 23]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''


'''
###
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
'''
####
'''galera = []
dado = list()
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
     if p[1] >=21:
         print(f"{p}")
     else:
         print("xxx")'''

####

'''dados = dict() #or dados = {}
dados = {'nome':'Pedro', 'idade':23, 'sexo': 'M'}
print(dados)
print(dados['sexo'])

filme = {'titulo':"Star Wars", 'ano':1997, 'diretor': 'Jorge Lucas'}
print(filme['ano'])
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
    '''
###
'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())
pessoas['peso'] = 98.5 #adicionar elemento
for k,v in pessoas.items():
    print(f"{k} = {v}")'''
###
'''brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brsil[1]['sigla'])'''
###
'''estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
print()
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor: {v}")
for v in e.values():
    print(v, end="")
print("Fim")'''

'''def traco():
    print('--'*20)


traco()
print("   Sistema de Alunos    ")
traco()
print('Testando funções')
traco()
print('Parametros')'''

'''def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
mensagem('INTRODUÇÃO A FUNÇÕES EM PY')'''



'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('   TESTE 1   ')
titulo('   TESTE 2   ')
titulo('   TESTE 3   ')'''


'''
def soma(a,b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(3, 4)'''


'''
def contador(*num):
    tam = len(num)
    print(f'{tam} numeros')


contador(2,4,5,6,7)
contador(3,5,6,7,9,0)
contador(12.2,4,5,76,8)'''


'''
def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,5,2,0,4]
dobra(valores)
print(valores)

print('xxx')'''



'''

def cont(i,f,p):
    """ Faz uma contagem e mostra na tela:
    i = inicio da contagem
    f = fim da contagem
    p = passo
    return = sem retorno
    """
    c =  i
    while c <= f:
        print(f'{c}', end=' / ')
        c += 1
    print('\nFIM!\n')

cont(0, 10, 2)
help(cont)

'''


'''
def somar(a = 0, b = 0, c = 0): #parametros opcionais
    s = a + b + c
    print(f'A SOMA VALE: {s}')

somar(2,3,4)
somar(3,5)
somar(a = 2*4, b = 1)

'''
'''
#Escopo de variáveis

def teste():
    x = 8
    print(f'Função teste, n vale {n}')




n = 2
print(f" Principal {2}")
teste()
'''
'''
#Retornando valores:

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = (somar(2, 2))
r3 = somar(6)
print(f"Os resultados são: {r1}, {r2} e {r3}.")
'''


'''
def fatorial(n=1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f

num = (int(input('DIGITE UM NUMERO: ')))
print(f'O fatoria de {num} é {fatorial(num)}') '''

