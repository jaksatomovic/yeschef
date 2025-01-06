from urllib.request import urlopen
from recipe_scrapers import scrape_html


# Example recipe URL
url = "https://www.coolinarika.com/recept/karnevalske-fritule-6b94210a-63f2-11eb-bacb-0242ac120016"
# retrieve the recipe webpage HTML
html = urlopen(url).read().decode("utf-8")

# pass the html alongside the url to our scrape_html function
scraper = scrape_html(html, org_url=url)

# Extract recipe information
print(scraper.title())          # "Spinach and Feta Turkey Burgers"
print(scraper.total_time())     # 35
print(scraper.yields())         # "4 servings"
print(scraper.ingredients())    # ['1 pound ground turkey', '1 cup fresh spinach...']
print(scraper.instructions())   # 'Step 1: In a large bowl...'


