#Exercicio semana 4 - Incerteza - Thiago Emanuel
from pomegranate import *

#Definindo probabilidade inicial (pensado a partir de probabilidades na cidade de Almenara)
inicio =  DiscreteDistribution({
  "sol": 0.8,
  "chuva": 0.2
})

#Definindo traniscoes do meteorológicas
meteorologias = ConditionalProbabilityTable([
  ["sol", "sol", 0.8],
  ["sol", "chuva", 0.2],
  ["chuva", "sol", 0.6],
  ["chuva", "chuva", 0.4]
], [inicio])

cadeiaDeMarkov = MarkovChain([inicio, meteorologias])

#Definindo o numero de amostras que vai ser gerada
numeroDeAmostras = 100

#Gerando amostrar usando a funcao sample do pomegranate
amostras = cadeiaDeMarkov.sample(numeroDeAmostras)

#Extrair informações (neste exemplo irei realizar o calculo da porcentagens das transições)
solEsol = 0 #probabiliddade de ter dia de sol depois de um dia de sol
chuvaEchuva = 0 #probabiliddade de ter dia de chuva depois de um dia de chuva
solEchuva = 0 #probabiliddade de ter dia de sol depois de um dia de chuva
chuvaEsol = 0 #probabiliddade de ter dia de chuva depois de um dia de sol


print(f'Imprimindo {numeroDeAmostras}" amostras')

print(amostras)

#Contar quantas ocorrencias de cada transicao teve
for i in range(numeroDeAmostras):
  if(i+1 < numeroDeAmostras):
      if amostras[i] == "sol" and amostras[i+1] == "sol":
          solEsol += 1 
      elif amostras[i] == "chuva" and amostras[i+1] == "chuva":
          chuvaEchuva += 1
      elif amostras[i] == "sol" and amostras[i+1] == "chuva":
          solEchuva += 1
      elif amostras[i] == "chuva" and amostras[i+1] == "sol":
          chuvaEsol += 1

print(" ")
#Imprimindo a quantidade de ocorrencia de cada transicao
print("Imprimindo a quantidade de ocorrencia das transicoes")

print(f'Quantidade de ocorrencia de ter dia de sol depois de um dia de sol: {solEsol}')

print(f'Quantidade de ocorrencia de ter dia de chuva depois de um dia de chuva: {chuvaEchuva}')

print(f'Quantidade de ocorrencia de ter dia de sol depois de um dia de chuva: {solEchuva}')

print(f'Quantidade de ocorrencia de ter dia de chuva depois de um dia de sol: {chuvaEsol}')

print(" ")
#Imprimindo as porcentagens
print("Imprimindo a porcentagem de ocorrencia das transicoes")

print(f'Probabiliddade de ter dia de sol depois de um dia de sol: {round((solEsol/numeroDeAmostras)*100,1)} %')

print(f'Probabiliddade de ter dia de chuva depois de um dia de chuva: {round((chuvaEchuva/numeroDeAmostras)*100,1)} %')

print(f'Probabiliddade de ter dia de sol depois de um dia de chuva: {round((solEchuva/numeroDeAmostras)*100,1)} %')

print(f'Probabiliddade de ter dia de chuva depois de um dia de sol: {round((chuvaEsol/numeroDeAmostras)*100,1)} %')
