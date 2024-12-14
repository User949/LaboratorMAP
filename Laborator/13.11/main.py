import requests
import smtplib
from email.mime.text import MIMEText

with open(r'Drumul catre fisierul in care este cheia API', 'r') as fisier:
    API_KEY = fisier.read().strip()

with open(r'Drumul catre fisierul in care este parola google', 'r') as fisier:
    parola_cont_google = fisier.read().strip()

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
URL_API = "https://api.openweathermap.org/data/2.5/weather"
oras = input("Introduceti numele orasului ")
units = "metric"

email = 'exemplu@gmail.com'
email_destinatar = 'exemplu2@gmail.com'

request_url = f"{URL_API}?q={oras}&appid={API_KEY}&units={units}"

def starea_vremii ():
    raspuns = requests.get(request_url)
    if raspuns.status_code == 200:
        data = raspuns.json()
        temperatura = data["main"]["temp"]
        umiditate = data["main"]["humidity"]
        status_vreme = data["weather"][0]["description"]
        return temperatura, umiditate, status_vreme
    else:
        print("Eroare pentru Request-ul tau!")
temp, umid, sts_vreme = starea_vremii()

def trimitere_email (temp, umid, sts_vreme):
    msg = MIMEText(f"Vreme: {sts_vreme}\nTemperatura: {temp}\nUmiditate: {umid}")
    msg['Subject'] = "Starea vremii de astazi"
    msg['From'] = "Starea vremii de astazi"
    msg['To'] = email_destinatar
    #Trimiterea efectiva a email-ului
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(email, parola_cont_google)
        smtp_server.sendmail(email, email_destinatar, msg.as_string())

trimitere_email(temp, umid, sts_vreme)
print(f"Temperatura pentru orasul {oras}: {temp}°C\nUmiditate: {umid}%\nDescriere vreme: {sts_vreme}")

#print(API_KEY)