# 🛠️ Projeto ETL com MongoDB e MySQL

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) que realiza:

- Extração de dados de uma coleção MongoDB
- Transformações com Pandas (renomeação, filtragem, formatação de datas)
- Exportação para CSV
- Carga final em tabelas relacionais no MySQL

---

## 🔄 Fluxo do Pipeline

1. **Extract**
   - Conexão com MongoDB
   - Filtros por categoria e por data (regex)
   - Extração de documentos da coleção

2. **Transform**
   - Criação de DataFrame a partir dos documentos
   - Renomeação de colunas
   - Conversão e padronização de datas

3. **Load**
   - Criação do banco de dados `db_products` e tabelas `books` e `products_from_2021`
   - Inserção dos dados transformados no MySQL
   - Exportação dos dados para arquivos `.csv`

---

## 🧪 Testes

Testes manuais foram realizados com um script em `tests/test_pipeline_manual.py`, cobrindo:

- Inserção e leitura no MongoDB
- Transformações com Pandas
- Exportação e inserção no MySQL

---

## 🧰 Tecnologias utilizadas

- Python 3.10
- MongoDB e PyMongo
- MySQL e mysql-connector-python
- Pandas
- Python-dotenv
- Jupyter Notebook
- **WSL2 (Windows Subsystem for Linux 2)**
---

## 📁 Estrutura do projeto

```bash
.
├── extract/
│   └── extract_data.py
├── transform/
│   └── transform_data.py
├── load/
│   └── load_data.py
├── tests/
│   └── test_pipeline_manual.py
├── data/
│   └── products_test.csv
├── .env
├── main.py
├── requirements.txt
└── README.md

```

---

## 📦 Pré-requisitos

Antes de executar o pipeline, é necessário:

### MongoDB
- Ter uma instância do MongoDB Atlas ou local funcionando
- Criar o banco de dados (por exemplo: `etl_pipeline`)
- Criar a coleção com os documentos de origem (ex: `collection_products`)
  - Ou executar o script de inserção de dados de teste, se houver

### MySQL
- Ter um servidor MySQL funcionando
- Criar o banco de dados `db_products`
  - As tabelas `books` e `products_from_2021` serão criadas automaticamente pelo script

### Variáveis de ambiente
Configure um arquivo `.env` na raiz do projeto com os seguintes campos:
- mongo_uri=mongodb+srv://<usuario>:<senha>@cluster.mongodb.net
- mysql_host=localhost
- mysql_user=seu_usuario
- mysql_password=sua_senha
- mysql_database=db_products

## ⚙️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. (Opcional) Insira dados de teste na coleção MongoDB:

```bash
python tests/test_pipeline_manual.py
```
⚠️ Esse script insere dados de teste e executa funções diretamente via `if __name__ == "__main__"`.
Caso **não deseje utilizá-lo**, deixe o bloco `if __name__ == "__main__"` **comentado** ou o arquivo desativado.

4. Execute o pipeline principal:

```bash
python main.py
```
📌 Caso você deseje montar o seu próprio fluxo, utilize as funções dos módulos extract, transform e load conforme necessário.

---

## 👩‍💻 Desenvolvido por

Luiza Vieira – Estudante de Análise e Desenvolvimento de Sistemas - Cesar School

- 💼 [LinkedIn](https://www.linkedin.com/in/vbluuiza)
- 💻 [GitHub](https://github.com/vbluuiza)
