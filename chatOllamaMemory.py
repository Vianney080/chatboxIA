from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time

template = """
Tu es professeur de science au lycee. Sois clair, concis et pedagogue.
Explique les reponses en utilisant des exemples simples et un langage adapte aux eleves de 15 ans.
Question: {question}
Reponse:
"""
model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handleConversation():
    context =""
    print("Bonjour je suis Alexandra, comment je peux vous aider ? Si vous n’avez pas de question, tapez'exit' pour quitter.")
    while True:
        user_input = input("Vous: ")
        if user_input.lower() == 'exit':
            print("Au revoir!")
            break
        
        context += f"Question: {user_input}\n"
        result = chain.invoke({"context":context,"question": user_input})
        
        for char in result:
            print(char, end='', flush=True)
            time.sleep(0.02)
        
        context += f"\nUser {user_input}: {result}\n"
        print("\n") 