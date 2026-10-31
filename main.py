import requests

#no hardcoring
with open('personality.txt','r',encoding="utf-8") as file:
    personality = file.read()

#dictionary [model name, prompt, stream setting]
data={
    "model":"qwen2.5:3b",}

messages = [
    {
        "role": "system",
        "content": personality
    }
]

while(True):
    prompt = input("\nEnter your prompt:\t")           #accepting user input

    if prompt == "exit":
        break
    
    messages.append({
        "role":"user",
        "content":prompt
    })
    
    chat_data = {
    "model": data["model"],
    "messages": messages,
    "stream": False}

    #Send a POST request to the API.
    response = requests.post("http://localhost:11434/api/chat", json = chat_data)
    reply = response.json()["message"]["content"]
    
    messages.append({
        "role":"assistant",
        "content":reply
    })
    
    #Read the response JSON and print its response field.
    print(f"{data['model']}:\t{reply}")