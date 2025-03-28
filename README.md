#### MVP Back-end
##### Estudante: ROBERTO TRAMONTINA ARAUJO
##### Matrícula: 4052024001752
##### Curso: DESENVOLVIMENTO FULL STACK
##### Disciplina: Sprint: Desenvolvimento Back-end Avançado (40530010060_20250_01)
# Título: Agenda Aniversariantes 
### Essa é uma alternativa para você, que assim como eu, não tem Facebook, Instagram ou qualquer outra mídia social e por isso perdeu a sua agenda de aniversários. 
### Com a Agenda Aniversariantes você tem uma forma segura e não invasiva de guardar essas datas e contatos especiais, sem a obrigação de se cadastrar em qualquer site.  

# Como executar - Modo Desenvolvimento
#### Instalar Python
#### Instalar Visual Studio Code (ou outra ferramenta conveniente)
#### Utilizar terminal Linux
#### Abrir VS Code e clonar o seguinte repositório: https://github.com/betotramontina/back-end-agenda-aniversariantes-adv.git  
#### Abrir docs em um terminal integrado e executar os seguintes comandos:
##### Criar ambiente virtual: python3 -m venv venv_api
##### Ativar ambiente virtual: source venv_api/bin/activate
##### Instalar os requisitos: pip install -r requirements.txt
##### Executar a API: flask run --host 0.0.0.0 --port 5000
##### Acessar API por meio do endereço http://172.20.51.164:5000/ 
##### Interagir com as rotas da API via Swagger

# Como executar - Via Docker
#### Abrir o terminal na raiz do seu projeto, onde o Dockerfile está localizado, e executar o seguinte comando como administrador: 'docker build -t nome-da-imagem .'
#### Em seguida, executar o seguinte comando como adm: 'docker run -p 5000:5000 nome-da-imagem'
#### Para interagir com a API, abrir o navegador e acessar: http://localhost:5000
