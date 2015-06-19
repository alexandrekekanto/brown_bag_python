#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Sintaxe básica
#

# Variávies
a = 1
b = "Bananas"
c = 13.42

array = [1, 2, 3, "Bananas", "Melancias"]
dicionario = {"bananas":3, "melancias":5, "goiabas":4}
# tupla é um array imutável
tupla = ("bananas", "goiabas", "melancias")

# if/else
if a == 1:
    print("a == 1")
else:
    print("a != 1")

# if/else multiplo, sem switch
if b == "Melancias":
    print ("b = Melancias")
elif b == "Bananas":
    print ("b = Bananas")
else:
    print ("b = nada")

# for basico
for i in range(10):
    print(i)

for i in array:
    print(i)

i = 0
while i < 10:
    print(i)
    i++


# funcao
def soma(a, b):
    return a + b

print(soma(10,5))

def exemplo(fruit="bananas", total=1):
    return "%d %s" % (total, fruit)

print(exemplo("melancia"))
print(exemplo(total=5))
print(exemplo(total=6, fruit="goiabas"))


# try/except
try:
    print("Try Bananas")
    raise Exception("No bananas for you")
except Exception as e:
    print("Deu merda ", e.message)
else:
    print("Deu certo")
finally:
    print("Terminou")


# with
with open("file.txt") as f:
    print(f.read())

# igual a
# f = open("file.txt")
# print(f.read())
# f.close()

## LISTAS
a = list(range(10))
len(a)
print(list() == [])

a[0]
a[0:2]
a[2:]
a[:-5]
a[-1]
a[:-1]
a.append(10)

## DICTS
b = 
