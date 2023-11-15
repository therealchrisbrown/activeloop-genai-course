from dotenv import load_dotenv
load_dotenv()

import openai

prompt_system = "Du bist ein hilfsbereiter Assistent, der bei der Beantwortung meiner E-Mails helfen soll. Du antwortest dabei immer in gereimter Form."
prompt = """Schreibe eine Antwort auf die folgende E-Mail, die nicht länger als 50 Wörter ist: 
Sehr geehrter Herr Christian Braun,
anbei erhalten Sie die Rechnung zu Ihrem Auftrag. 	 
Freundliche Grüße
"""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt_system},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)