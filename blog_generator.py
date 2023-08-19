import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["API_KEY"]

def generate_blog(paragraf_topic):
    response = openai.Completion.create(
        model='text-davinci-002',
        prompt='Escreva um paragrafo sobre o topico' + paragraf_topic,
        max_tokens=400,
        temperature=0.3
    )
    retrieve_blog = response.choices[0].text

    return retrieve_blog

#print(generate_blog("Quais são os maiores geradores de dopamina?"))

keep_writing = True
while keep_writing:
    answer = input('Escrever um paragrafo? S para sim e qualquer coisa para não. ')
    if (answer == 'S'):
        paragraf_topic = input('Sobre o que deve ser o paragrafo? ')
        print(generate_blog(paragraf_topic))
    else:
        keep_writing = False
