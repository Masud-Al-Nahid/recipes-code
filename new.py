from recipe_scrapers import scrape_me
import requests
from recipe_scrapers import scrape_html
from csv import writer



with open('recipe.csv', 'w', encoding='utf8', newline='') as file:

    #create new CSV file and write header that name Title ,Ingredients,instructions,nutrients,Image,link.
    thewriter = writer(file)
    header = ['Title', 'Ingredients', 'Instructions', 'Nutrition_Facts','image','links']
    thewriter.writerow(header)


    url = "https://www.allrecipes.com/recipe/220751/quick-chicken-piccata/"
    html = requests.get(url).content
    scraper = scrape_html(html=html, org_url=url)

    with open('recipe.csv', 'w') as info:
        infos = writer(info)
        thewriter.writerow([scraper.title(), scraper.ingredients(), scraper.instructions(), scraper.nutrients(), scraper.image(), scraper.links()])



