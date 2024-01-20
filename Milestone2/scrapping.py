from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, Safari, SafariOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from extractdate import datePostedFromMinute, datePostedFromHour, datePostedFromDay, datePostedFromMonth
from cwCSV import createCSV, writeJobPost, writeCSJ

chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the browser up in background
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')

browser = Chrome(options=chrome_options)

# options = SafariOptions()
# options.add_argument('--headless')
# browser = Safari(options=options)

def scrap(url):

    browser.get(url)
    html = browser.page_source
         
    # css-44l6ak
    doc = BeautifulSoup(html, "html.parser")
    if doc == None:
        return
    else:
        doc = doc.find(["main"], class_="css-44l6ak")
    # print(doc.prettify())

    # section1
    section1 = doc.find(["section"], class_="css-1yzinaq")

    if section1 == None:
        section1 = doc.find(["section"], class_="css-dy1y6u")
        
    s = section1.find(["span"], class_="css-6p4vp eoyjyou0")
    if(s == None):
        status = "Open"
    else:
        status = "Closed"

    jobTitle = section1.find(["h1"], class_="css-f9uh36").string

    jobType = section1.find(["span"], class_="css-ja0r8m eoyjyou0").string

    strong = section1.find(["strong"], class_="css-9geu3q")
    aTag = strong.find("div")

    companyName = aTag.next_element.text

    if companyName != "Confidential Company":
        companyLink = aTag.next_element["href"]
    else: 
        companyLink = "null"

    cl = strong.contents

    cl1 = cl[-1].split(", ")

    if cl1[1] != 'Egypt':
        jobRegion = cl1[0]
        jobCity = cl1[1]
        jobCountry = "Egypt"
    else:
        jobRegion = "null"
        jobCity = cl1[0]
        jobCountry = cl1[1]

    datePosted = section1.find(["span"], class_="css-182mrdn").text
    
    if "minute" in datePosted:
        minutes = int(datePosted.split(" ")[1])
        db = datePostedFromMinute(minutes)
    elif "hour" in datePosted:
        hours = int(datePosted.split(" ")[1])
        db = datePostedFromHour(hours)
    elif "day" in datePosted:
        days = int(datePosted.split(" ")[1])
        db = datePostedFromDay(days)
    elif "month" in datePosted:
        months = int(datePosted.split(" ")[1])
        db = datePostedFromMonth(months)
        
    # section2
    section2 = doc.find(["section"], class_="css-3kx5e2")
    
    jd1 = section2.find_all(["div"], class_="css-rcl8e5")
    jd = jd1[0]
    for jd in jd1:
        if jd.next_element.string == "Experience Needed:":
            ExperienceNeeded = jd.find("span", class_="css-47jx3m").string
        elif jd.next_element.string == "Career Level:":
            CareerLevel = jd.find("span", class_="css-47jx3m").string
        elif jd.next_element.string == "Education Level:":
            EducationLevel = jd.find("span", class_="css-47jx3m").string
        elif jd.next_element.string == "Salary:":
            Salary = jd.find("span", class_="css-47jx3m").string
             
    Salary = Salary.split(", ")[0]

    if ExperienceNeeded != "Not Specified":
        ExperienceNeeded = ExperienceNeeded.split(" ")
        if "More" in ExperienceNeeded:
            minimumExperience = int(ExperienceNeeded[2])
            maximumExperience = 'null'
        elif "to" in ExperienceNeeded:
            minimumExperience = int(ExperienceNeeded[0])
            maximumExperience = int(ExperienceNeeded[2])
        else:
            minimumExperience = int(ExperienceNeeded[0])
            maximumExperience = 'null'
    else:
        minimumExperience = 'null'
        maximumExperience = 'null'
        
    if CareerLevel == "Not Specified":
        CareerLevel = 'null'

    if EducationLevel == "Not Specified":
        EducationLevel = 'null'

    if Salary == 'Confidential' or Salary == 'Paid' or Salary == 'paid':
        minimumSalary = 'null'
        maximumSalary = 'null'
    else:
        Salary = Salary.split(" ")
        minimumSalary = int(Salary[0])
        maximumSalary = int(Salary[2])
        

    jobCategory = section2.find("div", class_="css-13sf2ik").find_all("span", class_="css-158icaa")
    jobCategory = [x.string for x in jobCategory]

    skills = section2.find("div", class_="css-s2o0yh").find_all("span", class_="css-158icaa")
    skills = [x.string for x in skills]
    
    # section 3
    # section3 = doc.find_all(["section"], class_="css-ghicub")
    # print(section3)

    jobDescription = doc.find(["div"], class_="css-1uobp1k")
    jobRequirement = doc.find(["div"], class_="css-1t5f0fr")
    
    if jobDescription == None:
        jobDescription = "null"
    else:
        jobDescription = jobDescription.get_text(separator="\n")
    
    if jobRequirement == None:
        jobRequirement = "null"
    else:
        jobRequirement = jobRequirement.get_text(separator="\n")
        

    jpRow = [[companyName, jobTitle, db, jobType, status, jobCountry, jobCity, jobRegion, minimumExperience, maximumExperience, minimumSalary, maximumSalary, EducationLevel, CareerLevel, jobDescription, jobRequirement]]
    
    jpcRows = []
    for jb in jobCategory:
        jpcRows.append([companyName, jobTitle, db, jb])
        
    jpsRows = []
    for s in skills:
        jpsRows.append([companyName, jobTitle, db, s])
        
    writeJobPost(jpRow, jpcRows, jpsRows)
    
    return companyLink, skills, jobCategory
    
    



skillSet = set()
jobCategorySet = set()
companyLinkSet = set()


# with open("links.txt") as f:
#     for url in f:
#         print(f"{j} - {url}")
#         j+=1
#         cl, s, jc = scrap(url.strip())
#         # print(i)
#         companyLinkSet.add(cl)
#         skillSet.update(s)
#         jobCategorySet.update(jc)
#         i+=1

# createCSV()
#  174
# link 632 has a problem

f = open("links.txt", 'r').readlines()
k = 1200
for i in range(k, 1395, 1):
    print(f"{i} - {f[i]}")
    cl, s, jc = scrap(f[i].strip())
    companyLinkSet.add(cl)
    skillSet.update(s)
    jobCategorySet.update(jc)
    
        
print("finished scrapping")
        
clRows = [[x] for x in companyLinkSet]
sRows = [ [x]for x in skillSet]
jcRows = [ [x] for x in jobCategorySet]

writeCSJ(clRows, sRows, jcRows)

browser.quit()
