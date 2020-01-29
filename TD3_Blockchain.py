import requests
from requests.auth import HTTPBasicAuth

r = requests.get("https://api.pro.coinbase.com/currencies")

def currencies():
    name=""
    L_currencies=[]
    r = requests.get("https://api.pro.coinbase.com/currencies")
    text=r.text
    for i in range(len(text)-4):
        if (text[i:i+4]=="name"):
            y=7
            name=""
            while(text[i+y]!='"'):
                name+=text[i+y]
                y=y+1
            L_currencies.append(name)
    print("Les monnaies disponibles sont: \n")
    for i in range(len(L_currencies)):
        print(str(i)+" : "+L_currencies[i])

currencies()








