# ChatBot para Responder Perguntas sobre Material de Ensino

## Descrição

Este projeto é um ChatBot desenvolvido em Python com uma interface web para responder perguntas sobre material de ensino submetido. Os arquivos podem ser enviados em formatos PDF, DOC, ou outros, e o ChatBot responderá com base nas informações contidas nos arquivos.

## Funcionalidades

- Submissão de arquivos através de uma interface web.
- Integração com a API da OpenAI para gerar respostas.
- Armazenamento do histórico de conversas em um banco de dados PostgreSQL.
- Implementação de RAG (Retrieval-augmented generation) para otimizar a busca e diminuir a alucinação.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-material-ensino.git
cd chatbot-material-ensino
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configure o banco de dados PostgreSQL e ajuste as configurações no arquivo `config.py`.

4. Execute a aplicação:

```bash
flask run
```

## Uso

1. Acesse a interface web em `http://localhost:5000`.
2. Submeta arquivos de ensino.
3. Faça perguntas sobre os arquivos submetidos.
4. O ChatBot responderá com base nas informações dos arquivos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT.