x = 1
k = 0
while True:
    if x > 5:
        break
    k = k + x
    if k >4 and k < 10:
        continue
    x = x + 1
    print(f'Valor de x é de {x}')
    print(f'Valor de K é de {k}')
