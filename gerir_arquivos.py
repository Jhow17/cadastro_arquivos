import csv
import operacoes
import codecs
import json


def to_JSON(dados_tupla):
    list_json = []
    
    for linha in dados_tupla:
        dict = {
            "id" : linha[0],
            "name" : linha[1],
            "price" : linha[2],
            "description" : linha[3],
        }
        list_json.append(dict)
    json_produtos = json.dumps(list_json, ensure_ascii=False, indent=4)
    return json_produtos



def ler_arquivos(arquivo):
    dados = []
    try :
        csv_file = csv.reader(codecs.iterdecode(arquivo.file, 'utf-8'))

        next(csv_file)
        
        for row in csv_file:
            dados.append((row[0], float(row[1]), row[2]))
            
        operacoes.cadastrar_banco(dados)
        return dados
    # pesquisar mais erros 
    except FileNotFoundError as e:
        print(f"No Found File {e}")
        
        
