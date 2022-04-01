#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno


# In[6]:


#Abrindo
file = 'municipio_tipo.csv'
data = pd.read_csv(file)
data 


# In[7]:


#  Observando linhas, colunas, tipos de dados e tamanho em mbs do dataset
data.info() # Tudo certo, tabela, tratada com todas linhas e colunas completas!


# In[ ]:


missingno


# In[8]:


# Agora eu selecionei  o ano e somei todas as motocicletas emplacadas naquele ano respectivo.
data2= data.groupby('ano').agg({'motocicleta': 'sum'}) #moto
data2


# In[9]:


#Criei esse array porque ao plotar meu gráfico , percebi que os anos no eixo X não estavam devidamente organizados, e apliquei
# logo em seguida
np.arange(2004,2021,1)


# In[10]:


#Por se tratar de uma série temporal usei o gráfico de linhas para melhor representar
plt.plot(data2, c= 'blue', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left') 

#Ajustando os eixos
plt.xticks(rotation = 60)
eixox= [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021]
plt.xticks([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021], eixox)
#tive alguns problemas com o eixo y quando se tratava de valores total por esse motivo fiz algumas adptações
eixoy = [1000000,10000000,20000000,30000000,40000000,50000000,60000000] 
plt.yticks([1000000,10000000,20000000,30000000,40000000,50000000,60000000], eixoy, rotation = 0)

# Legenda e cia 
plt.ylabel('Emplacamentos', fontsize = 13)
plt.title ('Emplacamentos de motos longo do tempo', color ='black', fontsize = 15)
plt.xlabel('Anos', fontsize = 13)
plt.show()


# In[11]:


# Agora iniciei a preparação para o gráfico de barras do total de motos emplacadas por ESTADOS
#Selecionei os estados e somei o total de motocicletas emplacadas em cada um deles
data3= data.groupby('sigla_uf').agg({'motocicleta': 'sum'}) #moto
data3


# In[12]:


# Usei o gráfico de barras para melhor representar o montante geral dos veículos emplacados no estados Brasileiros
data3.plot(stacked = True , kind = 'bar', color = 'limegreen', edgecolor = 'black', lw = 1 )
#se quiser rachurar o gráfico usa a função hatch


# ajustando eixos
plt.xticks(rotation = 66) # o eixo x = anos estavam deitados , mas ai consegui mecher nele e faze-lo deitar com a função rotation

#Aqui ó segredo é fazer um array baseado no maior número de seus dados
eixoy1 = [0,10000000, 20000000, 30000000, 40000000, 50000000, 60000000,70000000, 80000000, 90000000, 100000000, 110000000, 120000000, 130000000] # Aqui é o que vai no gráfico
plt.yticks([0,10000000, 20000000, 30000000, 40000000, 50000000, 60000000,70000000, 80000000, 90000000, 100000000, 110000000, 120000000, 130000000], eixoy1, rotation = 0)  # Aqui é o que você irá ditar
  

#Legenda e afins
plt.ylabel('EMPLACAMENTOS', fontsize = 13)
plt.title ('Emplacamento de motos nos estados', color ='black', fontsize = 15)
plt.xlabel('ESTADOS', fontsize = 13)
plt.show()


#Se quiser salvar o gráfico obs: ele vai direto pra pasta onde estão os dados
plt.savefig('gráficomotoest.png',dpi=500, bbox_inches = 'tight')


# In[13]:


# Eu observei se  essa  tendência de aumento de emplacamento ao longo dos anos segue em todos os estados do nordeste

# PB/RN e afins  = Selecionei  a COLUNA dos estados, logo após  seleicionei o ESTADO ESPECÍFICO (PB) e transformei em um DATA FRAME
# No data frame do estado selecionado, foi somado todos os emplacamentos de motos dos seus respectivos anos.

RN = data.loc[(data['sigla_uf'] == 'RN')]
RN2 = RN.groupby('ano').agg({'motocicleta': 'sum'})

PB  = data.loc[(data['sigla_uf'] == 'PB')]
PB2 = PB.groupby('ano').agg({'motocicleta': 'sum'}) 

PE = data.loc[data['sigla_uf'] == 'PE']
PE2 = PE.groupby('ano').agg({'motocicleta': 'sum'}) 

CE = data.loc[data['sigla_uf'] == 'CE']
CE2 = CE.groupby('ano').agg({'motocicleta': 'sum'}) 

BA = data.loc[data['sigla_uf'] == 'BA']
BA2 = BA.groupby('ano').agg({'motocicleta': 'sum'}) 

PI = data.loc[data['sigla_uf'] == 'PI']
PI2 = PI.groupby('ano').agg({'motocicleta': 'sum'}) 

MA = data.loc[data['sigla_uf'] == 'MA']
MA2 = MA.groupby('ano').agg({'motocicleta': 'sum'}) 

AL = data.loc[data['sigla_uf'] == 'AL']
AL2 = AL.groupby('ano').agg({'motocicleta': 'sum'}) 

SE = data.loc[data['sigla_uf'] == 'SE']
SE2 = SE.groupby('ano').agg({'motocicleta': 'sum'}) 


# In[22]:


#Emplacamento NE ao longo dos anos

plt.plot(RN2, c= 'red', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'RN') 
plt.plot(PB2, c= 'blue', ls = '--', lw = '2', marker ='^', ms=5, fillstyle = 'left',  label = 'PB') 
plt.plot(AL2, c= 'green', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'AL') 
plt.plot(PE2, c= 'yellow', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left',label = 'PE') 
plt.plot(PI2, c= 'pink', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'PI')
plt.plot(SE2, c= 'black', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'SE') 
plt.plot(CE2, c= 'orange', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'CE') 
plt.plot(BA2, c= 'gray', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'BA') 
plt.plot(MA2, c= 'purple', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'MA') 
plt.legend()


eixoy1 = [200000,600000, 1000000, 1500000,2000000,2500000,3000000]
plt.yticks([200000, 600000, 1000000,1500000,2000000,2500000,3000000], eixoy1, rotation=0)
eixox1= [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021]
plt.xticks([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021], eixox1, rotation = 90)
   

plt.ylabel('EMPLACAMENTOS', fontsize = 13)
plt.title ('Emplacamento de motos nos estados ao longo do tempo', color ='black', fontsize = 15)
plt.xlabel('ANOS', fontsize = 13)
plt.show()

# Mantiveram a mesma tendência dos gráficos nacionais.


# In[23]:


# Agora para observar por regiões brasileiras, eu selecionei cada estado  e somei o numero de motocicletas emplacadas


# Agora a região sudeste
SP = data.loc[(data['sigla_uf'] == 'SP')]
SP2 = SP.groupby('ano').agg({'motocicleta': 'sum'})

MG = data.loc[(data['sigla_uf'] == 'MG')]
MG2 = MG.groupby('ano').agg({'motocicleta': 'sum'})

RJ = data.loc[(data['sigla_uf'] == 'RJ')]
RJ2 = RJ.groupby('ano').agg({'motocicleta': 'sum'})

ES = data.loc[(data['sigla_uf'] == 'ES')]
ES2 = ES.groupby('ano').agg({'motocicleta': 'sum'})


# Região SUL
RS = data.loc[(data['sigla_uf'] == 'RS')]
RS2 = RS.groupby('ano').agg({'motocicleta': 'sum'})

PR = data.loc[(data['sigla_uf'] == 'PR')]
PR2 = PR.groupby('ano').agg({'motocicleta': 'sum'})

SC = data.loc[(data['sigla_uf'] == 'SC')]
SC2 = SC.groupby('ano').agg({'motocicleta': 'sum'})


#REGIÃO NORTE
AM = data.loc[(data['sigla_uf'] == 'AM')]
AM2 = AM.groupby('ano').agg({'motocicleta': 'sum'})

PA = data.loc[(data['sigla_uf'] == 'PA')]
PA2 = PA.groupby('ano').agg({'motocicleta': 'sum'})

AC = data.loc[(data['sigla_uf'] == 'AC')]
AC2 = AC.groupby('ano').agg({'motocicleta': 'sum'})

AP = data.loc[(data['sigla_uf'] == 'AP')]
AP2 = AP.groupby('ano').agg({'motocicleta': 'sum'})

RO = data.loc[(data['sigla_uf'] == 'RO')]
RO2 = RO.groupby('ano').agg({'motocicleta': 'sum'})

RR = data.loc[(data['sigla_uf'] == 'RR')]
RR2 = RR.groupby('ano').agg({'motocicleta': 'sum'})

TO = data.loc[(data['sigla_uf'] == 'TO')]
TO2 = TO.groupby('ano').agg({'motocicleta': 'sum'})


# CENTRO OESTE
GO = data.loc[(data['sigla_uf'] == 'GO')]
GO2 = GO.groupby('ano').agg({'motocicleta': 'sum'})

MT = data.loc[(data['sigla_uf'] == 'MT')]
MT2 = MT.groupby('ano').agg({'motocicleta': 'sum'})

MS = data.loc[(data['sigla_uf'] == 'MS')]
MS2 = MS.groupby('ano').agg({'motocicleta': 'sum'})

DF = data.loc[(data['sigla_uf'] == 'DF')]
DF2 = DF.groupby('ano').agg({'motocicleta': 'sum'})


# In[24]:


# Uni os respectivos estados  em um dataframe indicando as suas regiões  e depois somei 
Norte = AM2 + PA2 + AC2 + AP2 + RO2 + RR2 + TO2
Nordeste = RN2 + PB2 + CE2 + PI2 + MA2 + AL2 + SE2 + BA2 + PE2
Sul = RS2 + PR2 + SC2
Sudeste = SP2 + RJ2 + ES2
Centro = GO2 + MT2 + MS2 + DF2


# In[38]:


# Plotando os gráficos por regiões
plt.plot(Nordeste, c= 'red', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'NORDESTE') 
plt.plot(Sul, c= 'blue', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'SUL') 
plt.plot(Centro, c= 'orange', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'CENTRO OESTE') 
plt.plot(Sudeste, c= 'gray', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'SUDESTE') 
plt.plot(Norte, c= 'green', ls = '--', lw = '2', marker ='o', ms=5, fillstyle = 'left', label = 'NORTE') 
plt.legend()

eixoy2 = [100000,20000000,5000000, 10000000, 15000000]
plt.yticks([100000, 20000000,5000000, 10000000,15000000], eixoy2, rotation=0)
eixox2= [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021]
plt.xticks([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021], eixox2, rotation = 60)



plt.ylabel('EMPLACAMENTOS REGIÕES', fontsize = 13)
plt.xlabel('ANOS',fontsize = 13)
plt.title('Emplacamento de motos nas regiões Brasileiras', c = 'black', fontsize = 14)
plt.show ()

# Todos eles seguiram a mesma tendência de aumento até o ano de 2020 e queda no ano de 2021


# In[27]:


# Para fins de curiosidade quis observar se algum outro tipo de veículo não seguia esssa mesma tendência
Bonde = data.groupby('ano').agg({'bonde': 'sum'})
Onibus = data.groupby('ano').agg({'onibus':'sum'})


# In[40]:


plt.plot(Bonde, c= 'red', ls = '-', lw = '2', marker ='^', ms=6, fillstyle = 'left', label = 'Bonde') 
plt.plot(Onibus, c= 'blue', ls = '-', lw = '2', marker ='o', ms=6, fillstyle = 'left', label = 'Ônibus') 
plt.legend()

eixox2= [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021]
plt.xticks([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021], eixox2, rotation = 60)





plt.ylabel('EMPLACAMENTOS REGIÕES', fontsize = 13)
plt.xlabel('ANOS',fontsize = 13)
plt.title('Emplacamento de ônibus e bondes', c = 'black', fontsize = 14)
plt.show ()


# In[ ]:




