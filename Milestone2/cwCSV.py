import csv

def createCSV():

    fields = ["CompanyName", "JobTitle", "DatePosted", "JobType", "Status", "Country", "City", "Region", "MinimumExperience", "MaximumExperience", "MinimumSalary", "MaximumSalary", "EducationLevel", "CareerLevel", "JobDescription", "JobRequirements"]
    
    filename = "JobPost2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields) 
       
        
    fields = ["CompanyName", "JobTitle", "DatePosted", "JobCategory"]
    filename = "JobPostCategory2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields) 
    
    
    fields = ["CompanyName", "JobTitle", "DatePosted", "Skills"]
    filename = "JobPostSkills2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)
        
        
    fields = ["CompanyLink"]
    filename = "CompanyLinks2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)
    
        
    fields = ["SkillName"]
    filename = "Skills2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)
    
    fields = ["CategoryName"]
    filename = "JobCategories2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)
    

def writeJobPost(jpRow, jpcRows, jpsRows):
    
    filename = "JobPost2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(jpRow) 
        
    filename = "JobPostCategory2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(jpcRows) 
    
    filename = "JobPostSkills2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(jpsRows)
        

def writeCSJ(clRows, sRows, jcRows):
    
    filename = "CompanyLinks2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(clRows)
    
        
    filename = "Skills2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(sRows)
    
    filename = "JobCategories2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(jcRows)
    
        
    
def createCSV2():

    fields = ["CompanyName", "MinimumSize", "MaximumSize", "FoundationDate", "Country", "City", "CompanyURL", "CompanyDescription"]
    
    filename = "Company2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields) 
        
        
    fields = ["CompanyName", "Sector"]
    filename = "CompanySector2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)
        
    fields = ["SectorName"]
    filename = "Sectors2.csv"
    with open(filename, 'w', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(fields)

def writeCompany(cRow, csRows):
    
    filename = "Company2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(cRow) 
        
    if len(csRows) != 0:
        filename = "CompanySector2.csv"
        with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
            csvwriter = csv.writer(csvfile)  
            csvwriter.writerows(csRows)

def writeSector(sRows):
    
    filename = "Sectors2.csv"
    with open(filename, 'a', encoding='utf-8-sig') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerows(sRows) 

    


    