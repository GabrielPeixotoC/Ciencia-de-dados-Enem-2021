#!/usr/bin/env python
# coding: utf-8

# ## 1. Importação das bibliotecas padrões para tratamento de dados

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ## 2. Importação do dataset do enem 2021

# In[2]:


#descobrindo o encode dos dados
with open('microdados_enem_2021.csv') as f:
    print(f)


# In[3]:


get_ipython().run_cell_magic('time', '', "\ndf = pd.read_csv('microdados_enem_2021.csv', sep=';', encoding = 'cp1252')")


# ## 3. Conhecendo o dataset

# In[4]:


# mostrando as primeiras linhas
df.head()


# In[5]:


df.shape


# Aqui já da para ver que é um dataset bem grande com mais de 3 milhões de linhas, talvez para análise computacionais mais profundas seja necessário, em decorrencia das limitações da capacidade do meu computador pessoal, reduzir o dataset.

# In[6]:


df.dtypes


# Nos tipos é possível ver que há variáveis categóricas que estão sendo entendidas como numéricas, por exemplo, estado civil e número da inscrição. Tratarei disso no decorrer do estudo.

# In[7]:


df.columns


# In[8]:


df.describe()


# In[9]:


df['TP_FAIXA_ETARIA'].describe()


# ### Aqui causa uma estranhesa que terei que recorrer ao dicionário dos dados
# Por exemplo que média de faixa etária é igual a 5. Consulto a documentação do conjunto de dados e descubro que é realizado por categorias que abarcam um intervalo de idade.
# 
# Por exemplo, categoria 5 representa os 20 anos e categoria 20 representa pessoas com mais de 70 anos. Numa parte final de apresentação dos dados seria necessário apresentar essa informação ao apresentar os resultados da pesquisa.
# 

# In[10]:


df.isna().sum()


# ### Documentação da raça está em categoria também, por enquanto, vou deixar assim se necessário tentarei converter para outro tipo
# Por enquanto, basta entender que
#     0:	Não declarado,
#     1:	Branca,
#     2:	Preta,
#     3:	Parda,
#     4:	Amarela,
#     5:	Indígena, 
#     6:	Não dispõe da informação.
# 

# In[11]:


# conversão da raça para objeto do tipo texto, não quero que seja tratado como número, visto que representa apenas uma categoria


# In[12]:


df['TP_COR_RACA'] = df['TP_COR_RACA'].astype('str')


# In[13]:


df['TP_COR_RACA'].value_counts()


# Aqui vemos que o que mais aparece no conjunto de dados é 3 e 1, respectivamente, pardo e branco.

# In[14]:


df['TP_COR_RACA'].dtype


# ## 4. Convertendo todo dataframe para os tipos apropriados.

# In[15]:


df = df.astype("category")


# In[16]:


df.dtypes


# In[17]:


df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5','NU_NOTA_REDACAO']] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5','NU_NOTA_REDACAO']].astype('float')


# Como se pode ver eu optei por converter todo dataframe para object e depois converti apenas as colunas que possuem as notas para numerico

# In[18]:


df.dtypes


# ## Detectando valores ausentes

# In[19]:


df.isna().sum().sum()


# In[20]:


df.isnull().sum()


# In[21]:


df.describe()


# In[22]:


for i in df:
    x = ((df[i].isna().sum()/len(df[i]))*100).round(2)
    print('coluna ',i,'possui ',x,'% de valores ausentes')


# In[ ]:




