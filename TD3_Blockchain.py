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

    








