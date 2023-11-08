from dotenv import load_dotenv #By using dotenv, you can safely store sensitive information, such as API keys, in a separate file and avoid accidentally exposing it in your code. This is particularly important when working with open-source projects or sharing your code with others, as it ensures that the sensitive information remains secure.
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