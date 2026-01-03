from fastapi import FastAPI, File, UploadFile

import gerir_arquivos
import operacoes

app = FastAPI()


@app.get("/") #sinalizador de end point
async def root():
    return{"message":"Hello Niggass"}


@app.post("/uploadfile/") #sinalizador de end point
async def upload_csv(file : UploadFile = File(...)):
    dados = gerir_arquivos.ler_arquivos(file)
    print(dados)
    return   {"Itens Cadastrados no Banco": len(dados)}
    
    

@app.get("/produtos")
async def get_produtos():
    produtos = operacoes.get_all()
    return {"Produtos Cadastrados":produtos}

