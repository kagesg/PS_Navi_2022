#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Exercício 1
print(("=")*10+"Exercício 1"+("=")*10)

from math import *

count = 0

for i in range(1,int(5*pow(10,6)),1):

  if ((i % 2 == 0) and (i % 37 == 0) and (i % 49 == 0)):
    count += 1
print ("Entre o intervalo de 1 à 5 milhões há {} números que são pares, multiplos de 49 e multiplos de 37".format(count))


# In[3]:


#Exercício 2
print(("=")*10+"Exercício 2"+("=")*10)

from math import *
from numpy import mean

X = []

for i in range(0,10,1):
  if i % 2 == 0:
    X.append(pow(3,i)+7*factorial(i))
  else:
    X.append(pow(2,i)+4*log(i))

mean = mean(X)
maximun = max(X)
max_position = X.index(maximun)

print("Dado o vetor: {}\nSabemos que a posição do maior número é {}\nE a média dos valores do vetor é de {:.2f}".format(X,max_position,mean))


# In[2]:


#Exercício 3
print(("=")*10+"Exercício 3"+("=")*10)

dic_alunos = {"aluno_1":0,"aluno_2":0,"aluno_3":0,"aluno_4":0,"aluno_5":0}
aluno_max = 0

for i in range(1,6,1):
  x = float(input("Informe a nota do aluno" + str(i) + ":"))
  nome = "aluno_"+str(i)
  dic_alunos[nome]=x

aluno_max = max(dic_alunos, key = dic_alunos.get)

print("A maior nota da turma foi {:.1f} e é do {}!".format(dic_alunos[aluno_max],aluno_max))


# In[ ]:




