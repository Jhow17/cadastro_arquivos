# CSV <-> SQLite Converter

Ferramenta desenvolvida em Python para facilitar a migração de dados entre planilhas CSV e bancos de dados SQLite.

## 🚀 Funcionalidades
- **Importação:** Leitura de arquivos CSV com tratamento de dados (conversão de tipos).
- **Performance:** Uso de `executemany` para inserção otimizada de grandes volumes de dados.
- **Segurança:** Gerenciamento de transações (commit/rollback) para garantir integridade.
- **Exportação:** (Em desenvolvimento) Funcionalidade para gerar CSVs a partir do banco.

## 🛠️ Tecnologias
- Python 3
- SQLite3
- Biblioteca CSV (Standard Library)

## 📂 Estrutura do Projeto
- `main.py`: Orquestrador da leitura e gravação.
- `operacoes.py`: Lógica de CRUD e inserção em lote.
- `conection.py`: Gerenciamento centralizado da conexão com o banco.