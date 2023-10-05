import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_caption(input_text, sys_instruct):
    conversation = [
        {"role": "system", "content": sys_instruct},
        {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    generated_caption = response.choices[0].message['content']

    return generated_caption
