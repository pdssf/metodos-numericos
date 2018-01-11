# Author: Paulo Salgado
# 31/10/2017
# Método de Runge-kutta para o calculo de equaçoes diferenciais
# OBS.: estou a usando a constante de euler (e) com 3 casas de precisão
# OBS.2: todos os valores de entrada devem ser separados por um Enter
# OBS.3 nesse metodo eu mudei o que cada variavel significa, pra ficar mais coerente com o livro

from matplotlib import pyplot as plt
import math


def evaluate(t, y):
    return eval(f)


ordenada = []
abscissa = []
Y = 0.0
print('Algumas instucoes para o inicio do programa:\nt=t(0) T=t(f) y=y(0) Y=y(f)\n')
print('Importante! Sempre use espaço entre operadores\n')
print('funçoes trigonometricas devem ser escritas com o prefixo math.\n')

f = input('digite sua funcao:\n(dy/dt)= ')
f = f.replace(" e", "2.718")
print('{}'.format(f))
yo = float(input('digite seus valores iniciais y e t :\ny0= '))
to = float(input('t0= '))
steps = int(input('digite o numero de passos: '))
T = float(input('agora entre com o valor de T:\nt(f)= '))

h= (T-to)/steps

for i in range (0, steps, 1):
    ordenada.append(to)
    abscissa.append(yo)
    kst = evaluate(to, yo)    # first k
    knd = evaluate(to + h/2, yo+ (h*kst)/2)    # second k
    krd = evaluate(to + h/2, yo+ (h*knd)/2)    # third k
    kth = evaluate(to + h, yo+ (h*krd))        # fourth k
    Y = yo + (((kst+ 2*knd + 2*krd + kth)*h)/6)
    print('{:.3f}         {:.3f}'.format(to, Y))
    to += h
    yo = Y

print("valor da funcao Y(t) no ponto {:.4f} eh aproximadamente: {:.4f}".format(to, Y))
print('usando passos de {:.4f}' .format(h))

plt.plot(ordenada,abscissa)
plt.title('aproximaçoes pelo metodo de Runge-Kutta')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()