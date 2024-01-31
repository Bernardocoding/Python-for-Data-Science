import numpy as np
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dados=np.loadtxt(url,delimiter=',',skiprows=1,usecols=np.arange(1,6,1))
#arrays de diametro e peso das frutas
diametro_laranja=dados[:5000,0]
peso_laranja=dados[:5000,1]
diametro_toranja=dados[5000:,0]
peso_toranja=dados[5000:,1]

#criando um gráfico de linhas com matplotlib LARANJA

plt.subplot(1,2,1)
plt.plot(peso_laranja,diametro_laranja)
#identificando as linhas
plt.legend(['Laranja'])
#identificando os eixos
plt.xlabel('Peso')
plt.ylabel('Diametro')
#regressão linear do gráfico
X=peso_laranja
Y=diametro_laranja
n=np.size(peso_laranja) # encontrar a quantidade de elementos
a=(n*np.sum(X*Y)-np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b=np.mean(Y)-a*np.mean(X)
#reta
plt.plot(X,a*X+b)
#calcular a quão distante a reta está da linha 
print(np.linalg.norm(Y-(a*X+b)))


#criando um gráfico de linhas com matplotlib TORANJA

plt.subplot(1,2,2)
plt.plot(peso_toranja,diametro_toranja)
plt.legend(['Toranja'])
#identificando os eixos
plt.xlabel('Peso')
plt.ylabel('Diametro')
#regressão linear do gráfico
X=peso_toranja
Y=diametro_toranja
n=np.size(peso_toranja) # encontrar a quantidade de elementos
a=(n*np.sum(X*Y)-np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b=np.mean(Y)-a*np.mean(X)
#reta 
plt.plot(X,a*X+b)
#calcular a quão distante a reta está da linha 
print(np.linalg.norm(Y-(a*X+b)))




plt.show()














