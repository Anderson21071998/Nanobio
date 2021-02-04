#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd


# Essa primeira função é a main() a função principal, ela executa praticamente todos os códigos que se seguem, nessa primeira
# parte esta as variaveis de input(), que são as variaveis que irão guardar os diretórios dos arquivos principais como o dataframe sem as repetições, a lista contendo os aminoacidos e suas ligações, e a lista contendo todos os aminoacidos que apareceram drane a analise.
# 
# Em tese esse script deve devolver 3 arquivos do tipo csv, sendo esses arquivos um com a lista dos aminoacidos que aparecerão, com uma planilha correta e por ultimo um que tenha  numero de vezes que uma lização do mesmo tipo ocorreu

# In[29]:


def main():
    name = input('insira o diretório do arquivo: ')
    saida_1 = input('insira o diretório para saida do arquivo sem as repetições:\n ')
    saida_2 = input('insira o diretório para saida do arquivo com os aminoacidos:\n ')
    saida_3 = input('insira o diretório para saida do arquivo da lista de aminoacidos:\n ')
    resultado = limpa_dados(name)
    repete = aminoacidos_aparições(resultado)
    amino = amino_total(resultado)
    aparições, ami = amino[0], amino[1]
    aminoacido = aminoacidos(ami)
    repete.to_csv(saida_1)
    aparições.to_csv(saida_2)
    aminoacido.to_csv(saida_3)


# A função limpa_dados executa o principal papel dentro da linha de códigos, ela limpa todo o arquivo csv e organiza os ligantes e aminoacidos nas suas colunas corretas, para que assim possa facilitar para as outras funções do script

# In[30]:


def limpa_dados (dados):
    df = pd.read_csv(dados)
    Proteinas = {'ALA','ARG','ASN','ASP','GLU','CYS','GLY','GLN','HIS','LLE',
                 'LEU','LYS','MET','PHE','PRO','SER','TYR','THR','TRP','VAL'}
    
    filtro_from = df['From'].str.split(':',expand = True)[1].str[:3].isin(Proteinas)
    filtro_To = df['To'].str.split(':',expand = True)[1].str[:3].isin(Proteinas)
    ligante_from = df[filtro_To]['From'].copy()
    ligante_To = df[filtro_To]['To'].copy()
    df.loc[filtro_To,'From'] = ligante_To
    df.loc[filtro_To,'To'] = ligante_from
    
    df_final = df[filtro_from != filtro_To]
    return df_final


# A função de aminoacidos aparições irá mostrar o numero de vezes que aquela ligação com aquele tipo de ligação ocorreu

# In[31]:


def aminoacidos_aparições(df):
    dados = df
    aminoacidos,ligantes,tipo_ligação = list(dados['From'].str.split(':')),list(dados['To'].str.split(':')),list(dados['Types'])
    proteina, ligante, tipo, n, ligações = [],[],[],[],[]
    for i in range(len(ligantes)):
        ligação = (aminoacidos[i][1],ligantes[i][1],tipo_ligação[i])
        if ligação not in ligações:
            ligações.append(ligação)
            proteina.append(aminoacidos[i][1])
            ligante.append(ligantes[i][1])
            tipo.append(tipo_ligação[i])
            n.append(1)
        else:
            for l in range(len(proteina)):
                if (proteina[l],ligante[l],tipo[l]) == ligação:
                    n[l] = n[l] + 1
    data = {'Aminoacido':proteina, 'Ligante':ligante,'tipo de ligação':tipo, 'N° Ligações': n}
    df_retorna = pd.DataFrame(data, columns=['Aminoacido', 'Ligante', 'tipo de ligação','N° Ligações'])
    return df_retorna


# E a função amino_total irá apenas mostra quantas vezes aquele aminoacido apareceu com aquele tipo de ligação

# In[33]:


def amino_total(df):
    dados = df
    aminoacidos,ligantes,tipo_ligação = list(dados['From'].str.split(':')),list(dados['To'].str.split(':')),list(dados['Types'])
    proteina, ligante, tipo, n, ligações = [],[],[],[],[]
    for i in range(len(ligantes)):
        ligação = (aminoacidos[i][1],tipo_ligação[i])
        if ligação not in ligações:
            ligações.append(ligação)
            proteina.append(aminoacidos[i][1])
            tipo.append(tipo_ligação[i])
            n.append(1)
        else:
            for l in range(len(proteina)):
                if (proteina[l],tipo[l]) == ligação:
                    n[l] = n[l] + 1
    amino = proteina
    data = {'Aminoacido':proteina,'Tipo de ligação':tipo, 'N° Ligações': n}
    df_retorna = pd.DataFrame(data, columns=['Aminoacido', 'Tipo de ligação','N° Ligações'])
    return (df_retorna,amino)


# In[34]:


def aminoacidos(lista):
    aminoacido = []
    for i in range(len(lista)):
        if lista[i] not in aminoacido:
            aminoacido.append(lista[i])
    data = {"Aminoacidos": aminoacido}
    df_retorna = pd.DataFrame(data, columns = ['Aminoacidos'])
    return df_retorna

