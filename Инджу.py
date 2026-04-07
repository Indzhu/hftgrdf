for i in range(1, 11):
    print(i)

    for i in range(1, 16, 2):
     print(i)

    n = int(input())
for i in range(1, n+1, 2):
    print(i)

    for i in range(1, 11):
     print(i, "->", i**2)
 

    n = int(input())
s = 0
for i in range(1, n+1, 2):
    s += i
print(s)

n = int(input())
s = 0
for i in range(1, n+1):
    if i % 3 == 0:
        s += i
print(s)

n = int(input())
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

    n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

n = int(input())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)

n = int(input())
for i in range(1, n+1):
    if i % 10 == 5:
        print(i)

    n = int(input())
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

print("Простое" if is_prime and n > 1 else "Не простое")

a = int(input())
b = int(input())

nod = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        nod = i

print(nod)

n = int(input())

for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

        n = int(input())
s = 0

for digit in str(n):
    s += int(digit)

print(s)


n = input()
max_digit = 0

for d in n:
    if int(d) > max_digit:
        max_digit = int(d)

print(max_digit)


i = 1
while i <= 10:
    print(i)
    i += 1

    n = int(input())
i = 1

while i < n:
    print(i)
    i += 3


    n = int(input())
i = 1
s = 0

while i <= n:
    s += i
    i += 1

print(s)



