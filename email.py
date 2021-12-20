from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime

def enviar_email(mensagem, email):
    print("Enviando email...")
    
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = "rvxfkajypfucbhru"
    msg['From'] = "julioneto09@gmail.com"
    msg['To'] = email
    msg['Subject'] = "ALERTA DE OCORRÊNCIA"

    msg.attach(MIMEText(mensagem, 'plain'))  # add in the message body

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    server.login(msg['From'], password)  # Login Credentials for sending the mail


    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print("Email enviado com sucesso para %s" % (msg['To']))