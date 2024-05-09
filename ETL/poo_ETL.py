import json
import csv
class Dados:
    def __init__(self,dados):
 
     
        self.dados=dados
        self.nomes_colunas=self.__get_columns()
        self.qtd_linhas=self.__size_data()
        
    
    def __leitura_json(path):
        with open(path,'r') as file:
            dados_json=json.load(file)
        return dados_json

    def __leitura_csv(path):
        dados_csv=[]
        with open(path,'r') as file:
            spamreader=csv.DictReader(file,delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv  
     
    @classmethod     
    def leitura_dados(cls,path,tipo_dados):
        if tipo_dados=='csv':
            dados=cls.__leitura_csv(path)
        
        elif tipo_dados=='json':
            dados=cls.__leitura_json(path)
     
        return cls(dados) 
    
    def __get_columns(self):
        return list(self.dados[-1].keys()) 
    
    def rename_columns(self,key_mapping:dict):
        new_dados=[]

        for old_dict in self.dados:
            dict_temp={}
            for k,v in old_dict.items():
                dict_temp[key_mapping[k]]=v
            new_dados.append(dict_temp)

        self.dados=new_dados
        self.nome_colunas=self.__get_columns()
        
    def __size_data(self):
        return len(self.dados)
      
   
    def join(dadosA,dadosB):
        combined_list=[]
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list)
    
    def __tranformando_dados_tabela(self):
        dados_combinados_tabela=[self.nomes_colunas]
        for row in self.dados:
            linha=[]
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna,'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela        

    def salvando_dados(self,path):
        dados_combinados_tabela=self.__tranformando_dados_tabela()
        with open(path,'w') as file:
            writer=csv.writer(file)
            writer.writerows(dados_combinados_tabela)
    
        
        
#LEITURA
path_json='data_raw/dados_empresaA.json' #'../data_raw/dados_empresaA.json' ../ significa que estamos subindo uma pasta    
path_csv="data_raw/dados_empresaB.csv"

dadosA=Dados.leitura_dados(path_json,'json')
#print(dadosA.leitura_dados())
print(f'Números de linhas Dados A: {dadosA.qtd_linhas}')
print(f'Nome das colunas Dados A: {dadosA.nomes_colunas}')


print("-"*100)

dadosB=Dados.leitura_dados(path_csv,'csv')
#print(dadosB.leitura_dados())
print(f'Números de linhas Dados B: {dadosB.qtd_linhas}')
print(f'Nome das colunas Dados B: {dadosB.nomes_colunas}')
print("-"*100)

#TRANFORMANDO
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dadosB.rename_columns(key_mapping)
print(f'Novos nomes das colunas Dados B: {dadosB.nomes_colunas}')
print("-"*100)

#juntando
dados_fusao=Dados.join(dadosA,dadosB)
print(f'Números de linhas Dados A e Dados B fundidos: {dados_fusao.qtd_linhas}')
print(f'Nome das colunas Dados A e Dados B fundidos: {dados_fusao.nomes_colunas}')
print("-"*100)

#SALVANDO
path_dados_combinados='data_processed/dados_combinados2.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Caminho para o arquivo salvado: {path_dados_combinados}')







    
    
    
    

    