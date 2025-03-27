# Etapa 1: Imagem base
FROM python:3.9

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o contêiner
COPY . .

# Comando para iniciar o servidor Flask
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
