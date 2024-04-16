import requests
from bs4 import BeautifulSoup
def affichTitre(url,par1,par2):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    titre = soup.find(par1, class_="article-body")
    articles = titre.find_all(par2)
    tabTitre=[]
    if articles:
        for art in articles:
            for titre in art:
                tit=titre.text.strip()
                tabTitre.append(tit)
        return(tabTitre)
url1 = "https://www.lemondeinformatique.fr/actualites/lire-6-formations-en-ligne-pour-apprendre-python-74349.html"
result=affichTitre(url1,"div","h2")
print(result)
