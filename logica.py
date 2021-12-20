import RPi.GPIO as GPIO
import time
import email as email
import servidor_get as sget
import servidor_post as spost
import whatsapp as w
import ligar_lampadas as ligar
import random
#
#

lista = ['imagens/imagem1.jpg', 'imagens/imagem2.jpg','imagens/imagem3.jpg','imagens/imagem4.jpg','imagens/imagem5.jpeg',]

indice = random.randrange(1, 5)
imagem = lista[indice]

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(3, GPIO.IN) #Entrada digital #Sensor de presença
GPIO.setup(5, GPIO.IN) #Entrada digital #Sensor fotoelétrico
GPIO.setup(11, GPIO.OUT) #Saida digital #Iluminação
GPIO.setup(13, GPIO.OUT) #Saida digital #Câmera



sensor = 3 #GPIO = 3
ldr = 10 #GPIO = 5

dicionario = sget.servidor()
tempo = dicionario['tempo_funcionamento']
  
iluminacao = ligar.ligar_lampadas()
if iluminacao == True:
  GPIO.output(11, GPIO.HIGH)
else:
  GPIO.output(11, GPIO.LOW)


if sensor == 3:#if GPIO.input(3) == GPIO.HIGH:
  if ldr < 5 :#if GPIO.input(5) == GPIO.HIGH:
    GPIO.output(13, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(13, GPIO.LOW)
    #enviar email(colocar o código da lista)
    spost.enviar_relatorio([imagem])
    w.zap('+55'+dicionario['telefone'])
    if(dicionario['enviar_email']==1):
      email.enviar_email('Nova ocorrência',dicionario['email'])
  else:
      GPIO.output(11, GPIO.HIGH)
      time.sleep(.5)
      GPIO.output(13, GPIO.HIGH)
      time.sleep(5)
      GPIO.output(13, GPIO.LOW)
      #enviar email
      spost.enviar_relatorio([imagem])
      w.zap('+55'+dicionario['telefone'])
      if(dicionario['enviar_email']==1):
          email.enviar_email('Nova ocorrência ',dicionario['email'])
      time.sleep(tempo)
      GPIO.output(11, GPIO.LOW)

