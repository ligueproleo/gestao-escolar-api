# Imersão DevOps - Alura Google Cloud

Este projeto é uma API desenvolvida com FastAPI para gerenciar alunos, cursos e matrículas em uma instituição de ensino.

## Pré-requisitos

- [Python 3.10 ou superior instalado](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started/)

## Como Executar o Projeto

### Opção 1: Executando com Docker (Recomendado)

Esta é a forma mais simples e recomendada. Com o Docker instalado, você não precisa se preocupar com a versão do Python ou com as dependências do projeto.

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/ligueproleo/gestao-escolar-api.git
   cd gestao-escolar-api
   ```

2. **Construa a imagem Docker:**
   ```sh
   docker build -t gestao-escolar-api .
   ```

3. **Execute o contêiner:**
   ```sh
   docker run -d -p 8000:8000 --name gestao-escolar-container gestao-escolar-api
   ```

### Opção 2: Executando Localmente (Manual)

1. **Clone o repositório (se ainda não o fez):**
   ```sh
   git clone https://github.com/ligueproleo/gestao-escolar-api.git
   cd gestao-escolar-api
   ```

2. **Crie um ambiente virtual:**
   ```sh
   python3 -m venv ./venv
   ```

3. **Ative o ambiente virtual:**
   - No Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```

4. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Execute a aplicação:**
   ```sh
   uvicorn app:app --reload
   ```
   
## Acessando a API
   
Após executar a aplicação (com Docker ou localmente), a documentação interativa da API estará disponível no seu navegador. Use-a para testar todos os endpoints.
   
- **URL:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   
---

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação FastAPI.
- `models.py`: Modelos do banco de dados (SQLAlchemy).
- `schemas.py`: Schemas de validação (Pydantic).
- `database.py`: Configuração do banco de dados SQLite.
- `routers/`: Diretório com os arquivos de rotas (alunos, cursos, matrículas).
- `requirements.txt`: Lista de dependências do projeto.

---

- O banco de dados SQLite será criado automaticamente como `escola.db` na primeira execução.
- Para reiniciar o banco, basta apagar o arquivo `escola.db` (isso apagará todos os dados).

---
