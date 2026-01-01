import csv
import operacoes




def ler_arquivos(arquivo):
    dados = []
    try :

        with open(arquivo, 'r', encoding='utf-8') as file_csv:
            lista_csv = csv.reader(file_csv, delimiter=',')
            next(lista_csv)
            
            for linha in lista_csv:
                dados.append((linha))
            
            operacoes.cadastrar_banco(dados)
            
            print('Arquivo lido e gravado com sucesso!')
    except FileNotFoundError as e:
        print(f"No Found File {e}")
        
        
if __name__ == "__main__":
    ler_arquivos('produtos_exemplo.csv')