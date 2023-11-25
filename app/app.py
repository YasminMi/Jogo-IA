import os
import gtts
import pygame
import pyttsx3
from ouvir_microfone import ouvir_microfone
from time import sleep 

def reproduzir_audio(caminho_arquivo):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_arquivo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def cenaUm():
    caminho_historia = 'app/historia/'
    try:
        vozPython = pyttsx3.init()
        vozPython.setProperty('voice', 'pt-br')
        tutorial = 'A) Opta pela trilha à esquerda, onde o suave murmúrio de um riacho o atrai. B) Decide seguir à direita, onde as árvores, densas e misteriosas, parecem esconder segredos inexplorados.'
        vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
        vozPython.runAndWait()
            # Pausa a execução do programa por 1 segundo.
        audio = ouvir_microfone()
        if("alternativa" in audio): 
            audio = audio.replace("alternativa", "")
            opcao = audio[1]
            if "a" in opcao or "b" in opcao:
                caminho_arquivo_opcao = os.path.join(caminho_historia, f'fala{opcao}.txt')
                arquivo_audio_opcao = f'arquivo{opcao}.mp3'
                
                if not os.path.exists(arquivo_audio_opcao):
                    conteudo = open(caminho_arquivo_opcao, 'r').read()
                    executarN = gtts.gTTS(conteudo, lang='pt-br')
                    executarN.save(arquivo_audio_opcao)
                    reproduzir_audio(arquivo_audio_opcao)
                else:
                    reproduzir_audio(arquivo_audio_opcao)  # Se o arquivo já existe, reproduz o arquivo existente
            else:
                print('Opção inválida')
                return cenaUm()
        else:
            print('diga Alternativa')
            cenaUm()
    except Exception as erro:
        print('Erro: ', erro)
        sleep(3)
        cenaUm()
    pass

def cenaDois():
    caminho_historia = 'app/historia/'
    try:
        vozPython = pyttsx3.init()
        vozPython.setProperty('voice', 'pt-br')
        tutorial = 'C) Aceita o convite da sereia. D) Desconfia da sereia e observá-la.'
        vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
        vozPython.runAndWait()
            # Pausa a execução do programa por 1 segundo.

        audio = ouvir_microfone()
        if("alternativa" in audio): 
            audio = audio.replace("alternativa", "")
            opcao = audio[1]
            if "c" in opcao or "d" in opcao:
                caminho_arquivo_opcao = os.path.join(caminho_historia, f'fala{opcao}.txt')
                arquivo_audio_opcao = f'arquivo{opcao}.mp3'
                
                if not os.path.exists(arquivo_audio_opcao):
                    conteudo = open(caminho_arquivo_opcao, 'r').read()
                    executarN = gtts.gTTS(conteudo, lang='pt-br')
                    executarN.save(arquivo_audio_opcao)
                    reproduzir_audio(arquivo_audio_opcao)
                else:
                    reproduzir_audio(arquivo_audio_opcao)  # Se o arquivo já existe, reproduz o arquivo existente
            else:
                print('Opção inválida')
                return cenaUm()
        else:
            print('diga Alternataiva')
            cenaDois()
    except Exception as erro:
        print('Erro: ', erro)
        sleep(3)
        cenaDois()
    pass

def cenaTres():
    caminho_historia = 'app/historia/'
    try:
        vozPython = pyttsx3.init()
        vozPython.setProperty('voice', 'pt-br')
        tutorial = 'E) Seguir pelo riacho e encontrar a fada. F) Esperar até o anoitecer com a sereia.'
        vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
        vozPython.runAndWait()
            # Pausa a execução do programa por 1 segundo.

        audio = ouvir_microfone()
        if("alternativa" in audio): 
            audio = audio.replace("alternativa", "")
            opcao = audio[1]
            if "e" in opcao or "f" in opcao:
                caminho_arquivo_opcao = os.path.join(caminho_historia, f'fala{opcao}.txt')
                arquivo_audio_opcao = f'arquivo{opcao}.mp3'
                
                if not os.path.exists(arquivo_audio_opcao):
                    conteudo = open(caminho_arquivo_opcao, 'r').read()
                    executarN = gtts.gTTS(conteudo, lang='pt-br')
                    executarN.save(arquivo_audio_opcao)
                    reproduzir_audio(arquivo_audio_opcao)
                else:
                    reproduzir_audio(arquivo_audio_opcao)  # Se o arquivo já existe, reproduz o arquivo existente
            else:
                print('Opção inválida')
                return cenaTres()
        else:
            print('diga Alternativa')
            cenaTres()
    except Exception as erro:
        print('Erro: ', erro)
        sleep(3) 
        cenaTres()
    pass

def cenaQuatro():
    caminho_historia = 'app/historia/'
    try:
        vozPython = pyttsx3.init()
        vozPython.setProperty('voice', 'pt-br')
        tutorial = 'G) Aceita a orientação da Fada, trilhando o caminho da Fonte da Sabedoria.. H) Desconfia da Fada, escolhendo o caminho da Clareira da Intuição.'
        vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
        vozPython.runAndWait()
            # Pausa a execução do programa por 1 segundo.

        audio = ouvir_microfone()
        if("alternativa" in audio): 
            audio = audio.replace("alternativa", "")
            opcao = audio[1]
            if "g" in opcao or "h" in opcao:
                caminho_arquivo_opcao = os.path.join(caminho_historia, f'fala{opcao}.txt')
                arquivo_audio_opcao = f'arquivo{opcao}.mp3'
                
                if not os.path.exists(arquivo_audio_opcao):
                    conteudo = open(caminho_arquivo_opcao, 'r').read()
                    executarN = gtts.gTTS(conteudo, lang='pt-br')
                    executarN.save(arquivo_audio_opcao)
                    reproduzir_audio(arquivo_audio_opcao)
                else:
                    reproduzir_audio(arquivo_audio_opcao)  # Se o arquivo já existe, reproduz o arquivo existente
            else:
                print('Opção inválida')
                return cenaQuatro()
        else:
            print('diga Alternativa')
            cenaQuatro()
    except Exception as erro:
        print('Erro: ', erro)
        sleep(3)
        cenaQuatro()
    pass

def cenaCinco():
    caminho_historia = 'app/historia/'
    try:
        vozPython = pyttsx3.init()
        vozPython.setProperty('voice', 'pt-br')
        tutorial = 'I)Desbravador da Sabedoria. J) Herói da Coragem k) Feiticeiro dos Mistérios'
        vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
        vozPython.runAndWait()
            # Pausa a execução do programa por 1 segundo.

        audio = ouvir_microfone()
        if("alternativa" in audio): 
            audio = audio.replace("alternativa", "")
            opcao = audio[1]
            if "i" in opcao or "j" in opcao or "k" in opcao:
                caminho_arquivo_opcao = os.path.join(caminho_historia, f'fala{opcao}.txt')
                arquivo_audio_opcao = f'arquivo{opcao}.mp3'
                
                if not os.path.exists(arquivo_audio_opcao):
                    conteudo = open(caminho_arquivo_opcao, 'r').read()
                    executarN = gtts.gTTS(conteudo, lang='pt-br')
                    executarN.save(arquivo_audio_opcao)
                    reproduzir_audio(arquivo_audio_opcao)
                else:
                    reproduzir_audio(arquivo_audio_opcao)  # Se o arquivo já existe, reproduz o arquivo existente
            else:
                print('Opção inválida')
                return cenaCinco()
        else:
            print('diga Alternativa')
            cenaCinco()
    except Exception as erro:
        print('Erro: ', erro)
        sleep(3)
        cenaCinco()
    pass



if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente.
    vozPython = pyttsx3.init()  # Inicializa um objeto de voz usando a biblioteca pyttsx3.
    vozPython.setProperty('voice', 'pt-br')
    tutorial = 'Num reino mágico, você é um jovem aventureiro em busca de segredos lendários que só serão revelados por escolhas sábias. Ao entrar no Bosque Encantado, você se depara com uma bifurcação.'  # Atribui uma string à variável tutorial.
    vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
    vozPython.runAndWait()  # Executa a fala do texto definido na variável tutorial.
     
    cenaUm()  # Chama a função main para iniciar a execução do programa.
    vozPython = pyttsx3.init()  # Inicializa um objeto de voz usando a biblioteca pyttsx3.
    vozPython.setProperty('voice', 'pt-br')
    tutorial = 'Ao seguir o riacho, você encontra uma magníficas floresta. Uma sereia á beira do riacho o convida para a margem.'
    vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
    vozPython.runAndWait()  # Executa a fala do texto definido na variável tutorial.
    
    cenaDois()
    vozPython = pyttsx3.init()  # Inicializa um objeto de voz usando a biblioteca pyttsx3.
    vozPython.setProperty('voice', 'pt-br')
    tutorial = 'A sereia canta uma linda canção. Ela oferece duas opções.'
    vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
    vozPython.runAndWait()  # Executa a fala do texto definido na variável tutorial.

    cenaTres()
    vozPython = pyttsx3.init()  # Inicializa um objeto de voz usando a biblioteca pyttsx3.
    vozPython.setProperty('voice', 'pt-br')
    tutorial = 'O Encontro Mágico No coração da floresta, uma Fada apareec para perguntar qual Destino você escolhe.'
    vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
    vozPython.runAndWait()  # Executa a fala do texto definido na variável tutorial.

    cenaQuatro()
    vozPython = pyttsx3.init()  # Inicializa um objeto de voz usando a biblioteca pyttsx3.
    vozPython.setProperty('voice', 'pt-br')
    tutorial = 'Diante de três portas místicas com desafios únicos, qual você escolhe.'
    vozPython.say(tutorial)  # Instrui o programa a interpretar a string tutorial.
    vozPython.runAndWait()  # Executa a fala do texto definido na variável tutorial.

    cenaCinco()
    print('fim')