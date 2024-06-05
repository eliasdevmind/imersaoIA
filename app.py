from flask import Flask, render_template, request
from api import GeminiAPI
from markdown_converter import converter_md_para_html
from contexto import definir_contexto_gamer

app = Flask(__name__)


GOOGLE_API_KEY = 'SUA API_KEY' 
api = GeminiAPI(GOOGLE_API_KEY)

definir_contexto_gamer(api) 

@app.route('/', methods=['GET', 'POST'])
def gamer_chatbot():
    if request.method == 'POST':
        prompt = request.form['pergunta']
        resposta_ia = api.enviar_prompt(prompt)
        resposta_formatada = converter_md_para_html(resposta_ia)
        conversa = [(prompt, resposta_formatada)] 
        return render_template('index.html', conversa=conversa)
    return render_template('index.html', conversa=[])

if __name__ == "__main__":
    app.run(debug=True)
