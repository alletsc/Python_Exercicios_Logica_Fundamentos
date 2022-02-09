from pessoa import Pessoa

p1 = Pessoa('Stella', 28)
p2 = Pessoa('Caio', 29)


"""
# p1 != p2, because they are different objects (different memory locations)
print(p2)
print(p1)

atributo = nome
p1.nome = 'Maria'
print(p1.nome)

p2.nome = 'João'
print(p2.nome)
"""

print(p2.nome)
print(p1.falando)
print(p2)
p2.comer('Macarrão')
p2.falar('Oi')
p2.parar_comer()
p2.parar_comer()
p2.comer('Macarrão')
p2.parar_comer()
p2.falar("Olá, tudo bem?")
p2.parar_falar()
p2.comer('Arroz')
p2.parar_comer()
p2.parar_falar()

print(p1.ano)
print(Pessoa.ano)
