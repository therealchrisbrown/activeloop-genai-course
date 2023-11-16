from dotenv import load_dotenv
load_dotenv()

import openai

prompt_system = """Du bist ein Assistent, der bei der meine E-Mails dankend beantworten soll. 
Du endest deine Antwort mit einem Witz. Vor dem Witz setzt du ein ""P.S.:"" 
Die Antwort darf nicht länger als 50 Wörter sein."""

prompt = """Schreibe eine Antwort auf die folgende E-Mail: 

""Hallo Herr Braun,
anbei erhalten Sie die Rechnung zu Ihrem Auftrag. 	 
Freundliche Grüße
Max Mustermann""
"""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt_system},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)