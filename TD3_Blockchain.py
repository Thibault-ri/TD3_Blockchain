import requests
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

print(asso_id_nom("0x"))





def currencies():
    name=""
    y=7
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
        print(str(i+1)+" : "+L_currencies[i])



def bid_ask(Nom_emmet,Nom_final):
    r = requests.get("https://api.pro.coinbase.com//products/"+asso_id_nom(Nom_emmet)+"-"+asso_id_nom(Nom_final)+"/book")
    text=r.text
    print(text)

bid_ask("Cosmo","Loom Network")





