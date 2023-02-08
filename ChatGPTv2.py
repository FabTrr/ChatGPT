import openai

# Inicializa la API de OpenAI
openai.api_key = "Tu clave API de OpenAI aquí"

# Este loop permite realizar preguntas continuamente
while True:

    # Configura el modelo y el prompt
    model_engine = "text-davinci-002"
    prompt = input('Escribe tu consulta: ')

    if 'salir' in prompt or 'exit' in prompt:
        break

    # Genera una respuesta
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Imprime la respuesta generada
    print(response["choices"][0]["text"])
    print("\n")