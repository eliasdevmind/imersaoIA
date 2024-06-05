# Gemini Gamer Chatbox

## Visão Geral

O GameGenius Chatbox é uma ferramenta interativa projetada para ajudar jogadores a esclarecer dúvidas e obter insights sobre jogos. Esta aplicação Flask configura uma interface web para o chatbot, permitindo aos usuários interagir facilmente com ele.

## Funcionalidades Principais

1. **Flask App Setup**:
   - O código inicializa uma aplicação Flask para criar uma interface web para o chatbot.

2. **GeminiAPI Class**:
   - `__init__`: Configura a API do GenerativeAI com a chave fornecida, encontra um modelo adequado para geração de conteúdo e inicia uma sessão de chat com esse modelo.
   - `encontrar_modelo`: Procura por um modelo que suporte geração de conteúdo e o configura com configurações específicas de geração e segurança.
   - `enviar_prompt`: Envia um prompt para a sessão de chat e retorna a resposta do modelo de IA.

3. **Definir_contexto_gamer Function**:
   - Define o contexto inicial para o chatbot, especialmente voltado para gamers.

4. **Rotas Flask**:
   - Rota `'/'`: Renderiza a página inicial `'index.html'`, onde os usuários podem fazer perguntas e ver as respostas do chatbot.
   - Quando os usuários submetem uma pergunta, ela é enviada para a API do Gemini e a resposta é formatada como HTML antes de ser exibida na página.

## Dependências Necessárias

- Flask
- Google GenerativeAI Python Client Library

## Instalação das Dependências

Execute os seguintes comandos no terminal:


```
pip install Flask
pip install markdown
pip install google-generativeai

```


**Observações:**
Certifique-se de ter uma chave de API válida para o Google GenerativeAI e substitua `'Sua Chave Api KEI'` no código pelo valor correto.
