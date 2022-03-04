min = float(input('Digite a minutagem utilizada: '))

def calc_min(min, taxa):
    total_a_pagar = min * taxa
    return total_a_pagar

if min < 200:
    taxa = calc_min(min, 0.2)
elif min >= 200 and min <= 400:
    taxa = calc_min(min, 0.18)
else:
    taxa = calc_min(min, 0.15)

print(f'O valor a pagar é R${taxa:.2f}')
