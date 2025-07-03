# 1. Imagem base com Python 3.12 (slim para reduzir tamanho)
FROM python:3.12-slim-bookworm

# 2. Variáveis de ambiente (formato correto)
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# 3. Diretório de trabalho
WORKDIR /app

# 4. Instalação de dependências (cache otimizado)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia toda a estrutura do projeto
COPY . .

# 6. Porta da aplicação
EXPOSE 8000

# 7. Comando de execução para produção (sem --reload)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]