#deve-se baixar estas biblioetas antes da sua utilizaçao 
import speech_recognition as sr #biblioteca do reconheimento de fala

def ouvir_microfone(): #funçao que ouve e reconhee a fala   
    try:
        microfone = sr.Recognizer() #habilita o microfone  
        with sr.Microphone() as source:#com o objeto (sr) utilizamos a funçao (microphone) e atribuimos a variavel (source)  
            print('[ Diga alternativa para interagir comigo, e diga sua alternativa! ]')     
            microfone.adjust_for_ambient_noise(source)#chama o algoritmo de reduçao de ruidos              
            audio = microfone.listen(source, None, 5)#funçao q ouve oq foi dito e armazena na variavel                
            iniciador = microfone.recognize_google(audio,language='pt-BR').lower()#funçao de reconhecimento da fala/de padroes, base de dados do deep learning
        
            print("Você:~", iniciador)         
        return iniciador 
    except Exception as erro:
        print('houve um erro inexperado na captura do audio, [tente novemente mais tarde]\n\t= codigo de erro [001]')   
    pass
