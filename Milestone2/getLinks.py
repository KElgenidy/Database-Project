from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the browser up in background
chrome_options.add_argument('--incognito')

i = 0
pl = []
# read all the links for job posts
while True:
    
    url = f"https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?start={i}"
    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        html = browser.page_source
        browser.quit()
        
    
    doc = BeautifulSoup(html, "html.parser")
    links = doc.find_all(["a"], attrs={"rel":"noreferrer", "class":"css-o171kl"})
    
    if not links:
        print("last page reached")
        print(f"page = {i}")
        break
    
    for link in links:
        pl.append(link["href"])
        
    i += 1
       
# write them in text file
textfile = open("links.txt", "w")
for element in pl:
    textfile.write(element + "\n")
textfile.close()

print("done")