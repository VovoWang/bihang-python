from bihang.api import Bihang

client = Bihang.api_secret(api_key="", api_secret="")

r = client.buttonsButton({'name':"python button",'price':2,'price_currency':'BTC'})

print(r.button)
