import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com"
respuesta = requests.get("http://books.toscrape.com")
soup = BeautifulSoup(respuesta.text, "html.parser")

titulos = soup.find_all("h3")
precios = soup.find_all("p", class_="price_color")
lista_titulos = []
lista_precios = []
for titulo in titulos:
    lista_titulos.append(titulo.text)                  
for precio in precios:
    lista_precios.append(precio.text)
        
datos = {
    "titulo":lista_titulos,
    "precio":lista_precios
    
    
}
df = pd.DataFrame(datos)
df.to_excel("resultados.xlsx",index=False)