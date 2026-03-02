import requests
from bs4 import BeautifulSoup
# 1. Télécharger la page HTML
url = "http://books.toscrape.com"
reponse = requests.get(url)
 
# 2. Vérifier que la requête a réussi
if reponse.status_code != 200:
    print("Impossible de charger la page.")
else:
    # 3. Analyser le HTML avec BeautifulSoup
    soupe = BeautifulSoup(reponse.text, "html.parser")
 
    # 4. Trouver tous les articles (livres) de la page
    livres = soupe.find_all("article", class_="product_pod")
 
    print(f"Nombre de livres trouvés : {len(livres)}")
    print("-" * 50)
 
    # 5. Extraire le titre et le prix de chaque livre
    for i, livre in enumerate(livres, 1):
        titre = livre.h3.a["title"]
        prix  = livre.find("p", class_="price_color").text
        print(f"{i:2}. {titre[:45]:<45} | {prix}")
