import pyttsx3
import datetime
import speech_recognition as sr
import pyautogui as pa
import time
import pyperclip

# inicia o TTS
texto_fala = pyttsx3.init()

def falar(audio):
    texto_fala.setProperty("rate", 195)
    voices = texto_fala.getProperty("voices")
    texto_fala.setProperty("voice", voices[0].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

# Função para obter a hora atual
def tempo():
    hora_atual = datetime.datetime.now().strftime("%I:%M")
    falar(f"Agora são, {hora_atual}")
    print(f"Hora: {hora_atual}")
    
# Função para a data atual
def data():
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
        "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]  
    agora = datetime.datetime.now()
    dia = agora.day
    mes = meses[agora.month - 1] #pega o mes correspondente 
    ano = agora.year
    falar(f"Hoje é dia {dia} de {mes}, de {ano}!")
    print(f"Data: {dia} de {mes} de {ano}")
    
    
#Função para saudar o usuario
def bem_vindo():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        saudacao = "Bom dia Larissa! Bem vinda de volta!" 
    elif 12 <= hora < 18:
        saudacao = "Boa tarde Larissa! Bem vinda de volta!"
    else:
        saudacao = "Boa noite Larissa! Bem vinda de volta"  
    falar(saudacao) 
    
#Função para comando de voz
def microfone():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        rec.adjust_for_ambient_noise(source, duration=1)
        rec.pause_threshold = 1 # tempo de pausa antes de processar a fala
        try:
            audio = rec.listen(source)  
            print("Processando...") 
            comando = rec.recognize_google(audio, language="pt-BR")
            print(f"você disse: {comando}")  
            return comando.lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro na conexão: {e}")
            falar("Houve um problema na conexão. Por favor, tente novamente.")
            return None
        
#Função principal para processar os comandos
if __name__ == "__main__":
    bem_vindo()
    while True:
        print("Escutando...")
        comando = microfone()
        
        #verifica se o comando não é nulo
        if comando is None:
            continue
        
        #Se o usuario disser "Lana", o programa responde "Estou lhe ouvindo"
        if "lana" in comando:
            falar("Estou lhe ouvindo!")
            continue
        #responde outros comandos
        elif "como" in comando:
            falar("Estou bem! obrigado por perguntar.")
            falar("o que posso fazer para ajuda-la?")
        if "abrir" in comando:
            
            falar("tudo bem!")
            pa.PAUSE = 1
            pa.press("win")
            pa.write("Edge")
            pa.press("ENTER")
            pa.write("youtube.com") 
            pa.press("ENTER")
            time.sleep(8)
            falar("E agora? o que faço?")
            continue
        
        elif "coloque" in comando:
            
            falar("você que manda!")
            time.sleep(5)
            pa.click(x=1032, y=123)
            pa.write("Sete vidas")  
            pa.press("ENTER")
            time.sleep(3)
            pa.click(x=1157, y=322)
            time.sleep(5)
            pa.press("ENTER")
            
        elif "horas" in comando:
            tempo()
        elif "data" in comando:
            data()
        elif "volte" in comando:
            falar("Por quanto tempo devo esperar?")
            while True:
                resposta = microfone()
                if resposta and resposta.isdigit():
                    segundos = int(resposta)
                    falar(f"ok, voltarei em {segundos} segundos.")
                    time.sleep(segundos)
                    falar("Estou de volta, senhor!")
                    break
                else:
                    falar("Por favor, diga um numero valido.")
        elif "obrigado" in comando:
            falar("Tudo bem! Se precisar estou aqui!")
            quit()
        else:
            falar("Desculpe, não entendi o comando. pode repetir?")                       
        
        
                  