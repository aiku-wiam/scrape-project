import requests
from bs4 import BeautifulSoup
import csv  # Python importera maintenant la vraie bibliothèque standard

url = "http://books.toscrape.com"
reponse = requests.get(url)
soupe = BeautifulSoup(reponse.text, "html.parser")
livres = soupe.find_all("article", class_="product_pod")

# Ouvrir un fichier CSV en écriture
with open("livres.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Titre", "Prix"])  # En-tête

    for livre in livres:
        titre = livre.h3.a["title"]
        prix = livre.find("p", class_="price_color").text
        writer.writerow([titre, prix])

print("Fichier livres.csv créé avec succès !")