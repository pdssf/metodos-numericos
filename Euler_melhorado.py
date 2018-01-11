# Author: Paulo Salgado
# 31/10/2017
# Método de Euler para o calculo de equaçoes diferenciais
# OBS.: estou a usando a constante de euler (e) com 3 casas de precisão
# OBS.2: todos os valores de entrada devem ser separados por um Enter

from matplotlib import pyplot as plt
import math


def evaluate(t, y):
    return eval(f)

ordenada = []
abscissa = []

Y = 0.0
print('Algumas instucoes para o inicio do programa:\nt=t(0) T=t(f) y=y(0) Y=y(f)\nImportante! Sempre use espaço entre operadores')
print('funçoes trigonometricas devem ser escritas com o prefixo math.')
f = input('digite sua funçao:\n(dy/dt)= ')
f = f.replace(" e", "2.718")
print('{}'.format(f))

f_y = float(input('digite seus valores iniciais y e t :\ny0= '))
f_t = float(input('t0= '))
h = int(input('digite o numero de passos: '))
T = float(input('agora entre com o valor de T:\nt(f)= '))
passo = ((T-f_t)/h)

T+= passo
print('   t        valor Y(t(i))')

for i in range (0, h, 1):
    ant = evaluate(f_t, f_y)  #fn
    aprx = f_y + passo*ant # yn+ fn (aproximação de y n+1)
    post = evaluate(f_t+passo, aprx)
    Y = f_y +((ant + post) * (passo / 2))
    f_t += passo
    abscissa.append(Y)
    ordenada.append(f_t)
    print('{:.3f}         {:.3f}'.format(f_t, Y))
    f_y= Y

print("valor da função Y(t) no ponto {:.4f} é aproximadamente: {:.4f}".format(f_t, Y))
print('usando passos de {:.4f}' .format(passo))

plt.plot(ordenada,abscissa)
plt.title('aproximaçoes por euler aprimorado')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()
