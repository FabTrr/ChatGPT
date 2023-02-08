import openai

# Inicializa la API de OpenAI
openai.api_key = "Tu clave API de OpenAI aquí"

# Define el prompt o la pregunta a hacerle al modelo
prompt = "¿Cuál es tu nombre?"

# Utiliza el modelo de lenguaje GPT-3 para generar una respuesta
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Imprime la respuesta generada
print(response["choices"][0]["text"])