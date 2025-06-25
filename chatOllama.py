from langchain_ollama import OllamaLLM
import time 

model = OllamaLLM(model="mistral")
user_input = "Qui est le meilleur de football au monde ?"
result = model.invoke(user_input)

for char in result:
    print(char, end='', flush=True)
    time.sleep(0.02)

print() 