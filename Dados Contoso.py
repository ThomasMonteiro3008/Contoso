#!/usr/bin/env python
# coding: utf-8

# ####  Analisando os dados de vendas e produtos empresa Contoso
# 
#    A análise consiste em ler arquivos CSV, avaliar a unificação das colunas desses arquivos após uma filtragem criando um DataFrame mais completo para avaliação. Assim avaliando com cálculos direto com python para avaliar performances das lojas envolvidas e produtos vendidos.
#    
#    Por fim, exportando o arquivo para um novo documento em CSV com a tabela totalmente atualizada.
#    
#    Os arquivos utilizados nessa análise são da empresa fictícia Contoso, da Microsoft.
#    

# In[14]:


import pandas as pd


# In[4]:


vendas_contoso_df = pd.read_csv('Contoso - Vendas  - 2017.csv', sep=";")
produtos_contoso_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=";")
lojas_contoso_df = pd.read_csv('Contoso - Lojas.csv', sep=";")
clientes_contoso_df =  pd.read_csv('Contoso - Clientes.csv', sep=";")


clientes_contoso_df = clientes_contoso_df[['ID Cliente', 'E-mail']]
produtos_contoso_df = produtos_contoso_df[['ID Produto', 'Nome da Marca']]
lojas_contoso_df = lojas_contoso_df[['ID Loja', 'Nome da Loja']]

vendas_contoso_df = vendas_contoso_df.merge(produtos_contoso_df, on='ID Produto')
vendas_contoso_df = vendas_contoso_df.merge(lojas_contoso_df, on='ID Loja')
vendas_contoso_df = vendas_contoso_df.merge(clientes_contoso_df, on='ID Cliente')

vendas_contoso_df = vendas_contoso_df.rename(columns={'E-mail': 'E-mail do Cliente'})


display(vendas_contoso_df)


# #### Obtendo o cliente que mais teve compras realizadas:

# In[5]:


top_cliente = vendas_contoso_df['E-mail do Cliente'].value_counts()
print(top_cliente)

top_cliente.head().plot(figsize=(15,5))


# #### Qual loja mais vendeu produtos?

# In[6]:


top_loja = vendas_contoso_df.groupby('Nome da Loja').sum()
top_loja = top_loja[['Quantidade Vendida']]
display(top_loja)


# In[7]:


top_loja = top_loja.sort_values('Quantidade Vendida', ascending=False)
display(top_loja.head())

top_loja.head().plot(figsize=(15,5), kind='bar')


# #### Para mostrar a loja, como o nome da loja virou o índice da tabela, podemos usar o max():

# In[8]:


best_loja = top_loja['Quantidade Vendida'].max()
name_loja = top_loja['Quantidade Vendida'].idxmax()
print(name_loja, best_loja)


# #### Calcular o perentual de vendas devolvidas

# In[9]:


quantidade_vendida = vendas_contoso_df['Quantidade Vendida'].sum()
quantidade_devolvida = vendas_contoso_df['Quantidade Devolvida'].sum()

percentual_devolvido = quantidade_devolvida/quantidade_vendida

print('{:.2%}'.format(percentual_devolvido))


# #### Calcular a taxa de devolução apenas de uma loja específica, Contoso Europe Online.

# In[10]:


loja_contosoeuron = vendas_contoso_df[vendas_contoso_df['ID Loja'] == 306]

qtde_vendidas_euron = loja_contosoeuron['Quantidade Vendida'].sum()
qtde_devolvida_euron = loja_contosoeuron['Quantidade Devolvida'].sum()

percentual_euron = qtde_devolvida_euron/qtde_vendidas_euron
print('{:.2%}'.format(percentual_euron))


# #### Adicionar a planilha uma coluna para dia, mês e ano independentes.

# In[11]:


vendas_contoso_df['Data da Venda'] = pd.to_datetime(vendas_contoso_df['Data da Venda'], format= '%d/%m/%Y')

vendas_contoso_df['Ano da Venda'] = vendas_contoso_df['Data da Venda'].dt.year
vendas_contoso_df['Mês da Venda'] = vendas_contoso_df['Data da Venda'].dt.month
vendas_contoso_df['Dia da Venda'] = vendas_contoso_df['Data da Venda'].dt.day

#display(vendas_contoso_df)
#vendas_contoso_df.info()


# Necessitando aumentar o preço do produto de ID = 873(Contoso Wireless Laser Mouse E50 Grey) para 23

# In[12]:


nova_vendas_contoso_df =  pd.read_csv('Contoso - Cadastro Produtos.csv', sep=";")
nova_vendas_contoso_df = nova_vendas_contoso_df.set_index('Nome da Marca')
#display(nova_vendas_contoso_df)

#nova_vendas_contoso_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preço Unitario'] == 23

display(nova_vendas_contoso_df)


# In[13]:


vendas_contoso_df.to_csv('Dados Contoso 2017.csv', sep=';')


# In[ ]:




