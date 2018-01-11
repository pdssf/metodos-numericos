#!-*- conding: utf8 -*-

# Author: Paulo Salgado
# 17/09/2017
# Metodo de Euler para o calculo de equacoes diferenciais
# OBS.: estou a usando a constante de euler (e) com 3 casas de precisao
# OBS.2: todos os valores de entrada devem ser separados por um Enter

from matplotlib import pyplot as plt
import math

ordenada = []
abscissa = []

Y = 0.0
print('Algumas instucoes para o inicio do programa:\nt=t(0) T=t(f) y=y(0) Y=y(f)\n')
print('Importante! Sempre use espaco entre operadores\n')
print('funcoes trigonometricas devem ser escritas com o prefixo math.\n')
f = input('digite sua funcao:\n(dy/dt)= ')
f = f.replace(" e", "2.718")
print('{}'.format(f))

y = float(input('digite seus valores iniciais y e t :\ny0= '))
t = float(input('t0= '))
h = int(input('digite o numero de passos: '))
T = float(input('agora entre com o valor de T:\ntf= '))
passo = ((T-t)/h)

T += passo
print('t        valor Y(t(i))')

for i in range(0, h, 1):
    delta = eval(f)
    Y = y + delta*passo
    ordenada.append(t)
    abscissa.append(Y)
    print('{:.3f}         {:.3f}'.format(t, Y))
    y = Y
    t += passo

print("valor da funcao Y(t) no ponto {:.4f} eh aproximadamente: {:.4f}".format(t, Y))
print('usando passos de {:.4f}' .format(passo))

plt.plot(ordenada, abscissa)
plt.title('aproximacoes por euler')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()
