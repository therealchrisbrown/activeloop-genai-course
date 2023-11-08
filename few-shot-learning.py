from dotenv import load_dotenv
load_dotenv()

import os
import openai

#Prompt for summarization

prompt = """
Describe the following movie using emojis.


{movie}: """

examples = [
    {"input": "Titantic", "output": "🛳️🌊❤️🧊🎶🔥🚢💔👫💑"},
    {"input": "The Matrix", "output": "🕶️💊💥👾🔮🌃👨🏻‍💻🔁🔓💪"}
]

movie = " The wolf of wallstreet"
response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
                {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.format(movie=examples[0]["input"])},
        {"role": "assistant", "content": examples[0]["output"]},
        {"role": "user", "content": prompt.format(movie=examples[1]["input"])},
        {"role": "assistant", "content": examples[1]["output"]},
        {"role": "user", "content": prompt.format(movie=movie)},
  ]
)

print(response.choices[0].message.content)

