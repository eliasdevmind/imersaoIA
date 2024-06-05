import google.generativeai as genai

class GeminiAPI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = self.encontrar_modelo()
        self.chat = self.model.start_chat(history=[])

    def encontrar_modelo(self):
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return genai.GenerativeModel(model_name='gemini-1.0-pro',
                                            generation_config={'candidate_count': 1, 'temperature': 0.7},
                                            safety_settings={'HARASSMENT': 'BLOCK_NONE', 'HATE': 'BLOCK_NONE', 
                                                           'SEXUAL': 'BLOCK_NONE', 'DANGEROUS': 'BLOCK_NONE'})
        return None

    def enviar_prompt(self, prompt):
        response = self.chat.send_message(prompt).text
        return response
