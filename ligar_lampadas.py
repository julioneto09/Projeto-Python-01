import requests
import datetime


def ligar_lampadas():
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    dia = dias[datetime.datetime.today().weekday()]
    r = requests.get('https://9a6c-192-141-108-70.ngrok.io/api/horario/'+dia)
    resposta = r.json()[0]
    hora_atual = datetime.datetime.now().hour
    if(hora_atual >= resposta['inicio'] and hora_atual <= resposta['fim']):
        return False
    else:
        return True