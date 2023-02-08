# Chat GPT Readme 📋

Ejemplo simple de chat GPT en Python utilizando OpenAI.

Este ejemplo utiliza el modelo de lenguaje GPT-3 de OpenAI y realiza una pregunta. La respuesta generada por el modelo se imprime en la consola.

Recuerda reemplazar "Tu clave API de OpenAI aquí" con tu propia clave API de OpenAI. En la parte de "Pre-requisitos" te explico como conseguirla.

**La variable 'temperature'** es un parámetro utilizado en el proceso de generación de texto por parte del modelo de lenguaje GPT-3 de OpenAI. Su función es especificar la diversidad y la originalidad de la respuesta generada por el modelo. Un valor de temperatura más alto (por ejemplo, 1.0) resulta en respuestas más creativas y sorprendentes, mientras que un valor de temperatura más bajo (por ejemplo, 0.0) resulta en respuestas más predecibles y conservadoras. En el ejemplo, se establece la temperatura en 0.5, lo que significa que el modelo generará respuestas que son un equilibrio entre diversidad y originalidad.


Se utiliza "text-davinci-002" como modelo de lenguaje específico dentro de la plataforma OpenAI.

OpenAI ofrece varios modelos de lenguaje diferentes, cada uno con sus propios parámetros y capacidades. Al especificar "text-davinci-002" como el motor a utilizar, estamos indicando que queremos utilizar el modelo de lenguaje GPT-3 de OpenAI, específicamente la versión "Davinci".

**La variable 'max_tokens'** es un parámetro que controla la longitud máxima de la respuesta generada por el modelo de lenguaje GPT-3 de OpenAI. Se utiliza en la función openai.Completion.create para especificar la cantidad máxima de tokens (es decir, palabras o símbolos individuales) que se permitirán en la respuesta generada por el modelo. 
Si el modelo genera una respuesta que excede el límite establecido por max_tokens, se cortará la respuesta para que cumpla con el límite.

En el ejemplo, se establece max_tokens en 1024, lo que significa que la respuesta generada por el modelo no deberá exceder 1024 tokens. 
Esta restricción se utiliza para controlar la longitud de la respuesta y evitar que sea demasiado larga o detallada.

**La variable 'n=1'** en la función openai.Completion.create, indica la cantidad de respuestas que se deben generar por el modelo de lenguaje para una determinada pregunta o entrada. Al establecer n=1, se está indicando que se desea generar solo una respuesta para cada entrada.

Si se establece por ejemplo n=3, el modelo generaría tres respuestas diferentes para cada entrada. Esto puede ser útil cuando se espera obtener varias opciones de respuesta o en las que se desea tener una comprensión más amplia de las respuestas. Sin embargo, generar varias respuestas puede requerir más tiempo y recursos.

## Pre-requisitos

1- Instalar la librería OpenAI: pip install openai

2- Crear usuario en OpenAI y obtener credenciales para utilizar su API en: https://openai.com/api/

3- Luego del log In, ir a: https://platform.openai.com/

4- Click en "Personal", luego click en "View API keys"

5- Click en "Create new secret key", guaradrlo en la variable openai.api_key

