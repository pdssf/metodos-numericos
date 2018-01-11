# Author: Paulo Salgado
# 17/09/2017
# Método de Euler inverso para o calculo de equaçoes diferenciais
# OBS.: estou a usando a constante de euler (e) com 3 casas de precisão
# OBS.2: todos os valores de entrada devem ser separados por um Enter

import math
from matplotlib import pyplot as plt

abscissa = []
ordenada = []

Y = 0.0
print('Algumas instucoes para o inicio do programa:\nt=t(0) T=t(f) y=y(0) Y=y(f)\n')
print('Importante! Sempre use espaço entre operadores\n')
print('funçoes trigonometricas devem ser escritas com o prefixo math.\n')
f = input('digite sua funcao:\n(dy/dt)= ')
f = f.replace(" e", "2.718")
print('{}'.format(f))

y = float(input('digite seus valores iniciais y e t :\ny0= '))
t = float(input('t0= '))
h = int(input('digite o numero de passos: '))
T = float(input('agora entre com o valor de T:\nt(f)= '))
passo = ((T-t)/h)

T += passo
ordenada.append(t)
abscissa.append(y)
print('  t         valor Y(t(i))')
for i in range (0, h, 1):
    delta = eval(f)  # fn
    aprx = y + delta*passo  # aproximação de yn+1
    ordenada.append(t)
    t += passo    # tn+1
    y, aprx = aprx, y
    Y= aprx + passo*eval(f)
    y = Y
    abscissa.append(Y)
    print('{:.3f}         {:.3f}'.format(t, Y))

print("valor da funcao Y(t) no ponto {:.4f} eh aproximadamente: {:.4f}".format(t, Y))
print('usando passos de {:.4f}' .format(passo))

plt.plot(ordenada,abscissa)
plt.title('aproximaçoes por euler inverso')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()