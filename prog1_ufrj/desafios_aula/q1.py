n1 = 3
n2 = 2
n3 = 1
# 3 < 2 < 1
if n1 >= n2 and n1 >= n3:
    print(n1)
if n2 > n3:
    print(n2)
    print(n3)
else:
    print(n2)
    print(n3)
print()

# n1 < n2 and n1 < n3:
# 1 < 2 < 3

a1 = 1
a2 = 3
a3 = 2

if a2 >= a1:
    print(a2) # 3
if a3 >= a2:
    print(a3) # 2
    print(a1) # 1
else:
    print(a3) # 2
    print(a1) # 1

print()

# n1 > n2 and n3 > n2:
# 3 > 2 and 4 > 3

b1 = 1
b2 = 2
b3 = 3

if b3 >= b2:
    print(b3) # 3
if b2 >= b1:
    print(b2) # 2
    print(b1) # 1
else:
    print(b2) # 2
    print(b1) # 1


