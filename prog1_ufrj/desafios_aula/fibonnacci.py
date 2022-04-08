num = int(input("Enter a number: "))
cont = 1

fib1 = 1
fib2 = 1

while cont <= num:
    fib_n = fib1 + fib2
    print(fib_n)
    fib2 = fib1
    fib1 = fib_n
    cont += 1


