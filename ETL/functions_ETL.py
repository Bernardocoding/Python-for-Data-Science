#leitura de dados json
import json
import csv



def leitura_json(path_json):
    with open(path_json,'r') as file:
        dados_json=json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv=[]
    with open(path_csv,'r') as file:
        spamreader=csv.DictReader(file,delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv        

def leitura_dados(path, tipo_arquivo): # função de junção dos dois tipos de leitura
    if tipo_arquivo=='csv':
        dados=leitura_csv(path)
        
    else:
        dados=leitura_json(path)
    return dados 

def get_columns(dados):
    return list(dados[0].keys()) 

def rename_columns(dados,key_mapping:dict):
    new_dados_csv=[]

    for old_dict in dados_csv:
        dict_temp={}
        for k,v in old_dict.items():
            dict_temp[key_mapping[k]]=v
        new_dados_csv.append(dict_temp)

    return new_dados_csv    

def size_data(dados):
    return len(dados)   

def join(dadosA,dadosB):
    combined_list=[]
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def tranformando_dados_tabela(dados,nomes_colunas):
    dados_combinados_tabela=[nomes_colunas]
    for row in dados:
        linha=[]
        for coluna in nomes_colunas:
            linha.append(row.get(coluna,'Indisponível'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela        

def salvando_dados(dados,path):
    with open(path,'w') as file:
        writer=csv.writer(file)
        writer.writerows(dados)

#LEITURA
path_json='data_raw/dados_empresaA.json' #'../data_raw/dados_empresaA.json' ../ significa que estamos subindo uma pasta    
path_csv="data_raw/dados_empresaB.csv"

dados_json=leitura_dados(path_json,'json') 
nome_colunas_json=get_columns(dados_json)
tamanho_dados_json=size_data(dados_json)
print(f'Nome de colunas json--> {nome_colunas_json}') 
print(f'Tamanho dos dados json--> {tamanho_dados_json}')           
print("-"*100)
dados_csv=leitura_dados(path_csv,'csv')
nome_colunas_csv=get_columns(dados_csv)
tamanho_dados_csv=size_data(dados_csv)
print(f'Nome de colunas cvs--> {nome_colunas_csv}')
print(f'Tamanho dos dados csv--> {tamanho_dados_csv}')    


#TRANFORMAÇÃO DOS DADOS
print("-"*100)
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_csv=rename_columns(dados_csv,key_mapping)
nome_colunas_csv=get_columns(dados_csv)
print(nome_colunas_csv)

#juntando os dados
dados_fusao=join(dados_csv,dados_json)
nome_colunas_fusao=get_columns(dados_fusao)
tamanho_dados_fusao=size_data(dados_fusao)
print(f'Nome de colunas fusao--> {nome_colunas_fusao}')
print(f'Tamanho dos dados fusao--> {tamanho_dados_fusao}')

#SALVANDO OS DADOS
path_dados_combinados='data_processed/dados_combinados2.csv'
dados_fusao_tabela=tranformando_dados_tabela(dados_fusao,nome_colunas_fusao) #tranforma o dicionário em tabela
print(dados_fusao_tabela[0:3])
salvando_dados(dados_fusao_tabela,path_dados_combinados)

