import requests
from bs4 import BeautifulSoup
from hashlib import new
import smtplib

from apscheduler.schedulers.blocking import BlockingScheduler



with open(r'Drumul catre fisierul in care este parola google', 'r') as fisier:
    parola_google = fisier.read().strip()

#print(parola_google)

to_addr_list = ['exemplu1@gmail.com'] #adresa care primeste email-ul
cc_addr_list = ['']
sender = 'exemplu2@gmail.com' #adresa care trimite email-ul
subject = 'A scazut pretul la produsul dorit'
counter = 0

def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'smtp.gmail.com:587'
        header = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, parola_google)
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except Exception as e:
        print("A aparut o eroare in trimiterea email-ului")
        return False

def scrape():
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup.prettify())
    print(soup.find_all('p'))
    #p.product-new-price

def verificare_pret():
    global counter
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    pret = soup.find('p', attrs={'class':'product-new-price'}).text
    pret = pret[0:5]
    pret = pret.replace(".", "")
    pret = int(pret)
    pretDeReferinta = 7200
    titlul_produsului = data_nume()
    ratingul_produsului = rating_produs()
    if (pret < pretDeReferinta and counter == 0):
        print("Pretul a scazut")
        mesaj = f"Pretul actual: {pret} RON\n"
        mesaj += f"Pretul de referinta: {pretDeReferinta} RON\n"
        mesaj += f"Titlul produsului: {titlul_produsului}\n"
        mesaj += f"Produsul are un rating de: {ratingul_produsului}"
        sendemail(sender, mesaj, subject, to_addr_list, cc_addr_list=[])
        counter += 1
    else:
        print("Pretul este mai mare decat pretul de referinta")


def data_nume():
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    nume_produs = soup.find('h1', attrs={'class':'page-title'}).text
    return nume_produs

def rating_produs():
    url = "https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    rating = soup.find('p', attrs={'class':'review-rating-data'}).text
    return rating


scheduler = BlockingScheduler()
scheduler.add_job(verificare_pret, 'interval', seconds = 10)
scheduler.start()

#scrape()

#verificare_pret()

#sendemail(sender, 'HELLO2', subject, to_addr_list, cc_addr_list)