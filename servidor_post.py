import requests

#-Criar um relatório-#

def enviar_relatorio(imagens):

    arquivo = {}
    for index, img in enumerate(imagens):
        arquivo['image['+str(index)+']'] = open(img, 'rb')

    print('Enviando arquivos...')

    payload = {'observacao': 'Nova ocorrência identificada'}
    try:
        x = requests.post('https://9a6c-192-141-108-70.ngrok.io/api/relatorio', data=payload, files=arquivo)
        print('Upload enviado com sucesso')
    except:
        print('Falha no upload')