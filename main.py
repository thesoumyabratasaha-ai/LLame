import requests

#no hardcoring
with open('personality.txt','r',encoding="utf-8") as file:
    personality = file.read()

#dictionary [model name, prompt, stream setting]
data={
    "model":"qwen2.5:3b",
    "prompt":"",
    "stream":False,
    "system":personality}

while(True):    
    data["prompt"]=input("\nEnter your prompt: ")           #accepting user input

    if data["prompt"] == "exit":
        exit(0)

    #Send a POST request to the API.
    response = requests.post("http://localhost:11434/api/generate", json=data)

    #Read the response JSON and print its response field.
    print(f"Qwen:\t{response.json()['response']}")