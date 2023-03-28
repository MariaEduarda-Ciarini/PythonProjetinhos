def priFunc():
    print("Python é melhor?")
priFunc()

def segFunc(nome):
    print("Olá, %s" %(nome))
segFunc("Amiguinhos do GitHub.")

def AdcN(Prinum, Segnum, Tercnum):
    print("Primeiro Número: " + str(Prinum))
    print("Segundo Número: " + str(Segnum))
    print("Terceiro Número extra: " + str(Tercnum))
    print("Somatoria de tudo: ", Prinum + Segnum + Tercnum)
AdcN(4600, 3660, 2000)



var_abol = 10 # Global Variável
def multiply(num1, num2):
    var_abol = num1 * num2 # Local Variável
    print(var_abol)
multiply(685, 6)
print(var_abol)

var_abol = 10
def multiply(num1, num2):
    var_loca = num1 * num2
    print(var_loca)
multiply(200, 31)
# o var_loca não serve de nada ali

idade = int(input("Digite sua idade usúario: "))
if idade > 16:
    print("Sim, você tem acesso, aproveite!")

# Expressão Lambda Função
def potc(num):
    resultado = num ** 2
    return resultado
print(potc(90))
print(potc(140))
print(potc(280))

#  Duas linhas
def poten(num):
    return num **2
print(poten(23))
print(poten(12))
print(poten(22))
print(poten(80))
print(poten(91))

# Uma linha

powtc = lambda num: num **2
print(powtc(412))
print(powtc(214))
print(powtc(892))

max_num = lambda x, y: x if x > y else y
result = max_num(2003, 2023)
print(result)

min_num = lambda x, y: x if x < y else y
result = min_num(991, 1002)
print(result)

abs_num = lambda x: x if x >= 0 else -x
result = abs_num(-1009.21)
print(result)

quadratic = lambda a, b, c, x: a*x**2 + b*x + c
result = quadratic(7, 6, 4, 5)
print(result)

is_even = lambda x: True if x % 2 == 0 else False
result = is_even(92)
print(result)

factorial = lambda x: 1 if x <= 1 else x * factorial(x-1)
result = factorial(3.14)
print(result)

square_root = lambda x: x**0.5
result = square_root(12741)
print(result)

lessNum = lambda z,n: z - n
lessNum(2003, 2023)
