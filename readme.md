# Métodos numericos - cin ufpe

Informações gerais:
	Na implementação dos métodos foi usada a linguagem Python 3 versão 3.5.3 bem como as bibliotecas math e matplotlib. 
	
	Todas as entradas são lidas direto do terminal ou da linha de comando dependendo do ambiente, elas devem ser separadas por um enter. É importante que todos os operadores aritméticos sejam escritos, por exemplo, ‘4y’ deve ser escrito na forma ‘4*y’. É saudável ainda adicionar espaço e parêntesis quando necessário, principalmente se envolver o NÚMERO DE EULER, pois é feita uma substituição do caractere ‘e’ por 2,718.
Funções matemáticas: É usado o set de funções básicas padrão do python, i.e. {soma, subtração, divisão, multiplicação e exponenciação}, mais as funções disponíveis na biblioteca math, como logaritmos, seno, cosseno, exponencial… Para as funções da biblioteca math deve-se incluir o prefixo math. na escrita, exemplo:

sen(4t) = math.sin(4*t)
log( y ) = math.log10(y)

A lista completa de funções e sintaxe pode ser encontrada em: https://docs.python.org/3/library/math.html

Variáveis: As únicas variáveis permitidas são ‘y’ e ‘t’, ambas devem ser instanciadas dessa forma, em caixa baixa. É usado a função eval(), que faz a substituição da variável pelo seu valor correspondente, portanto deve-se seguir esse padrão para o funcionamento pleno do programa.

Número de Euler: O número de Euler ‘e’ pode ser instanciado de duas formas, a primeira é usando a letra ‘e’ precedida de um espaço, isto é, escrevendo ‘ e’, nesse caso é feita uma substituição do caractere ‘e’ pelo número 2,718 antes de ser computado o método. O espaço faz-se necessário para evitar que um caractere seja substituído erroneamente, por exemplo no uso da função math.exp() onde o caractere ‘e’ de “exp” não representa o número de Euler. Um segundo modo é usando math.e, onde será retornado o número de Euler, é recomendado o uso da segunda forma, por questões de segurança e  precisão.

Gráfico: É usado a biblioteca matplotlib, mais especificamente a função pyplot que toma o valor de dois vetores contendo os pontos de t e de y, e os plota em um plano, a documentação da biblioteca pode ser encontrada em: https://matplotlib.org/users/

Entrada: A entrada padrão é a mesma, a sequência é:
equação diferencial: Na forma (dy/dt)= f(y,t) 
y inicial (y0)
t inicial (t0)
Número de passos (h)
t final (tf)

Saída: Sequencialmente é exibido no terminal a função tomada, e em seguida h linhas, exibindo o valor de y e t no passo correspondente. Por fim é mostrado uma mensagem contendo os valores aproximados da solução,e em seguida uma tela surgirá mostrando o gráfico gerado pela função.

Duvidas/sugestões enviar para pdssf@cin.ufpe.br
