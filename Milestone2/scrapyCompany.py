import csv
import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from cwCSV import createCSV2, writeCompany, writeSector


chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the driver up in background
# chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
driver =  Chrome(options=chrome_options)


# =
# PROXY = "11.456.448.110:8080"
# chrome_options = WebDriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome = webdriver.Chrome(chrome_options=chrome_options)

def scrapCompany(url):
    
    driver = Chrome(options=chrome_options)
    
    driver.get(url)
    try:
        span_element = driver.find_element(By.CLASS_NAME, "css-1jb4aod")
        span_element.click()
    except:
        print("there is no See More button")
    html = driver.page_source
    driver.quit()
        
    doc = BeautifulSoup(html, "html.parser")
    
    #  find(["div"], class_="css-12e2e2p").
    
    companyName = str(doc.find(["h1"], class_="css-12s37jy").text)

    profile_section = doc.find(["div"], id="profile-section")
    # print(profile_section.prettify())

    cp = profile_section.find_all("span", class_="css-16heon9")

    location = "null"
    sectors = "null"
    companySize = "null"

    for i in range(0, len(cp), 1):
        if i == 0:
            # get the location
            location = cp[i].string.split(", ")
            if len(location) == 1:
                companyCity = "null"
                companyCountry = location[0]
            else:
                companyCity = location[0]
                companyCountry = location[1]
        elif i == 1:
            sectors = cp[i].find_all("a")
            sectors = [x.string for x in sectors]
        elif i == 2:
            companySize = cp[i].string
        else:
            break

    if "-" in companySize:
        companySize = companySize.split(" ")[0].split("-")
        minimumSize = int(companySize[0])
        maximumSize = int(companySize[1])
    elif "More" in companySize:
        companySize = companySize.split(" ")
        minimumSize = int(companySize[2])
        maximumSize = "null"
    else:
        minimumSize = 'null'
        maximumSize = 'null'
    
    foundation = profile_section.find(["span"], class_="css-6whuzn")

    if foundation == None:
        foundation = "null"
    else:
        foundation = foundation.string        

    companyDescription = doc.find(["p"], class_="css-1ceuc1v")

    if companyDescription == None:
        companyDescription = 'null'
    else:
        companyDescription = str(companyDescription.text)
        
    url_soup = doc.find("a", class_="css-cttont")
    if(url_soup is not None):
        url = url_soup.get('href')
        
    # ["CompanyName", "MinimumSize", "MaximumSize", "FoundationDate", "Country", "City", "CompanyDescription"]
    
    cRow = [[companyName, minimumSize, maximumSize, foundation, companyCountry, companyCity, url, companyDescription]]
    
    csRows = []

    if sectors != "null":
        for s in sectors:
            csRows.append([companyName, s])
        
    writeCompany(cRow, csRows)
    driver.quit()
    time.sleep(0.5)
    return sectors
        
       
# createCSV2()
sectors = set()

# 136, 137, 213, 236
# f = open('/Users/karimsherif/Documents/Database/FM2/FM2CompanyLinks.csv').readlines()
# j = 501
# for i in range(j, 534, 1):
#     print(f'{j} - {f[i].strip()}')
#     s = scrapCompany(f[i].replace(" ", ""))
#     if s != "null":
#         sectors.update(s)
#     j+=1
    

# url = "https://wuzzuf.net/jobs/careers/WhiteHouseNannies,Inc.-Egypt-95344"
# url = "https://wuzzuf.net/jobs/careers/HoneywellInternational,Inc.-UnitedArabEmirates-94736"
# url = "https://wuzzuf.net/jobs/careers/HalliburtonEnergyServices,Inc.-Egypt-95343"
url = "https://wuzzuf.net/jobs/careers/Nile Bits, LLC.-Egypt-95302"
s = scrapCompany(url)
if s != "null":
    sectors.update(s)
   
# with open("/Users/karimsherif/Documents/Database/FM2/FM2CompanyLinks.csv", 'r') as file:
#   csvreader = csv.reader(file).
#   for i in range(j, 140, 1):
#     print(csvreader)
    
    

print("finished scrapping")

sRows = [ [x]for x in sectors]
writeSector(sRows)
driver.quit()