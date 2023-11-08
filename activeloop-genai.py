from dotenv import load_dotenv
load_dotenv()

import os
import openai

#Englisch Text to translate
english_text = "Hello, how are you?"

response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'Translate the following English text to German: "{english_text}"'}
    ],
)

print(response['choices'][0]['message']['content'])