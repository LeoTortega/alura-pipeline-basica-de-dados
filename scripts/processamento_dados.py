import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
      
    def leitura_json(self):
        with open(self.path, 'r') as file:
            dados_json = json.load(file)

        return dados_json

    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        
        return dados_csv

    def leitura_dados(self):
        dados = []
        if self.tipo_dados == 'csv':
            dados =self.leitura_csv()
        elif self.tipo_dados == 'json': 
            dados = self.leitura_json()
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        return dados
    
    def get_columns(self):
        return list(self.dados[0].keys())
    
    def rename_columns(self, key_mapping):
        self.dados = [{key_mapping[old_key]: value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.nome_colunas = self.get_columns()

    def join(dados_a, dados_b):
        combined_list = []
        combined_list.extend(dados_a.dados)
        combined_list.extend(dados_b.dados)

        return Dados(combined_list, 'list')
    
    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]
        dados_combinados_tabela.extend([[row.get(coluna, 'Indisponivel') for coluna in self.nome_colunas] for row in self.dados])

        return dados_combinados_tabela
    
    def salva_dados(self, path):
        dados = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados)
