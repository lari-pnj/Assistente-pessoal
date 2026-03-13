import speech_recognition as sr
import webbrowser
import os
import pyautogui
import pyttsx3
from fuzzywuzzy import fuzz

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
    
nome_assistente = "robotinica" 
falar(f"Olá, eu sou {nome_assistente}. Como posso ajudar você hoje?")   
    
    
def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        comando = reconhecedor.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except:
        return ""

def executar_comando(comando):
    # Abrir Sites
    dicionario_sites = { "abrir youtube music": ["youtube", "music"],
                        "abrir gemini": ["gemini", "gemine","gemi"],
                        "abrir notion": ["notion", "noti"]}
    
    if 'abrir youtube music' in comando:
        webbrowser.open("https://music.youtube.com/")
    
    elif 'abrir gemini' in comando:
        webbrowser.open("https://gemini.google.com")

    # Abrir Apps (Caminho do executável)
    elif 'abrir notion' in comando:
        os.startfile(r"C:\Users\SEU_USUARIO\AppData\Local\Programs\Notion\Notion.exe")

    # Clicar em algo específico (Exemplo: Botão de Play)
    elif 'clicar no play' in comando:
        # Você precisa saber a coordenada X e Y ou usar uma imagem de referência
        pyautogui.click(x=500, y=400) 

# Loop principal
while True:
    comando = ouvir()
    if 'desligar assistente' in comando:
        falar("Até mais, tenha um ótimo dia!")
        break
    executar_comando(comando)