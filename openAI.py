import os
import openai



openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = input(" Please give the AI a prompt!")

response = openai.Completion.create( engine="text-davinci-002", prompt=prompt, temperature=0.7, max_tokens=709, top_p=1, frequency_penalty=0, presence_penalty=0)

print(response.choices[0].text)

while(prompt != "exit"):
    prompt = input("Type 'exit' if you want to stop, else ask it more: ")
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=0.7, max_tokens=709,
                                        top_p=1, frequency_penalty=0, presence_penalty=0)
    print(response.choices[0].text)