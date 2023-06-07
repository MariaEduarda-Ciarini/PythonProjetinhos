primos = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
pares = lambda x: x % 2 == 0

primos = list(filter(primos, range(2,101)))
pares = list(filter(pares, range(2,101)))

print("Numeros primos até 100:", primos)
print("Numeros pares até 100:", pares)
