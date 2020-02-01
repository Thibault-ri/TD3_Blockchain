import requests,json
from requests.auth import HTTPBasicAuth

r = requests.get("https://api.pro.coinbase.com/currencies")




def asso_id_nom(nom):
    name=""
    Id=""
    x=5
    y=7
    L_currencies=[]
    L_Id=[]
    ind=0
    r = requests.get("https://api.pro.coinbase.com/currencies")
    text=r.text
    for i in range(len(text)-4):
        if (text[i:i+2]=="id"):
            x=5
            Id=""
            while(text[i+x]!='"'):
                Id+=text[i+x]
                x=x+1
            L_Id.append(Id)
            ind=ind+1
        elif (text[i:i+4]=="name"):
            y=7
            name=""
            while(text[i+y]!='"'):
                name+=text[i+y]
                y=y+1
            if(name==nom):
                break

            L_currencies.append(name)    
    return(L_Id[ind-1])







def currencies():
    currencies = requests.get('https://api.pro.coinbase.com/products')
    r_json = json.loads(currencies.text)
    L_c=[]
    curr=""
    print("Les monnaies disponibles sont: \n")
    for i in r_json:
        curr=i['base_currency']
        if curr not in L_c:
            L_c.append(curr)
            print(str(len(L_c))+" : "+curr)
        


def getDepth(direction='ask', pair = 'BTC-USD'):
    r = requests.get("https://api.pro.coinbase.com//products/"+pair+"/book")
    text_j=json.loads(r.text)
    print(text_j[direction+'s'])

    
def refreshDataCandle(pair = 'BTC-USD', duration = '5m'):
    unite_temps=duration[len(duration)-1]
    rtime=int(duration[0:len(duration)-1])
    L_u=[1,60,3600,3600*24,3600*24*7,3600*24*7*4]
    if unite_temps=="m":
        rtime=rtime*60
    elif unite_temps=="h":
        rtime=rtime*3600
    elif unite_temps=="d":
        rtime=rtime*3600*24
    elif unite_temps=="w":
        rtime=rtime*3600*24*7
    elif unite_temps=="M":
        rtime=rtime*3600*24*7*4
    elif unite_temps=="s":
        rtime=rtime
    else:
        print("erreur: unité incorrecte veuillez entrer le numero correspondant à l'unité desirée: \n 1-Seconde\n 2-Minute\n 3-Heure\n 4-Jour\n 5-Semaine\n 6-Mois(4 semaines)\n")
        choix=input()
        rtime=rtime*L_u[choix-1]  
    
    r = requests.get("https://api.pro.coinbase.com//products/"+pair+"/candles?granularity="+str(rtime))
    #text_j=json.loads(r.text)
    print(r.text)

refreshDataCandle()  








