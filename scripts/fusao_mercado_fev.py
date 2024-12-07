from processamento_dados import Dados

def main():
    path_json = 'data_raw/dados_empresaA.json'
    path_csv = 'data_raw/dados_empresaB.csv'

    # Extract
    dados_empresaA = Dados(path_json, 'json')
    print(f"Dados empresa A: {dados_empresaA.dados[0]}\n")

    dados_empresaB = Dados(path_csv, 'csv')
    print(f"Dados empresa B: {dados_empresaB.dados[0]}\n")
    
    print(f"Nome colunas dados empresa A: {dados_empresaA.nome_colunas}\n")
   
    print(f"Nome colunas dados empresa B: {dados_empresaB.nome_colunas}\n")

    key_mapping = {
        'Nome do Item':'Nome do Produto',
        'Classificação do Produto': 'Categoria do Produto',
        'Valor em Reais (R$)': 'Preço do Produto (R$)',
        'Quantidade em Estoque': 'Quantidade em Estoque',
        'Nome da Loja': 'Filial',
        'Data da Venda': 'Data da Venda'
    }

    # Transform
    dados_empresaB.rename_columns(key_mapping)

    print(f"Nome novas colunas dados csv: {dados_empresaB.nome_colunas}\n")

    dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

    # Load
    path_dados_combinados = 'data_processed/dados_combinados.csv'

    dados_fusao.salva_dados(path_dados_combinados)

    print('Dados carregados com sucesso!')

if __name__ == '__main__':
    main()