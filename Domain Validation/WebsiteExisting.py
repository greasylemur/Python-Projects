import requests
import csv
import time

Fuego=[]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

file = open('gooddomain.csv', 'w')
file.close()

def AddToList(domaintest):
    file = open('gooddomain.csv', 'a')
    file.write(domaintest)
    file.write("\n")
    file.close()
    print(domaintest)

def DoesExist(domaintest):
    if domaintest.endswith('.com'):
        try:
            request = requests.get(domaintest, headers=headers)
            if request.status_code == 200:
                Fuego.append([domaintest])
                AddToList(domaintest)
            else:
                print('Web site does not exist')
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except requests.exceptions.InvalidURL:
            requests.status_code = "Connection refused"
#       except requests.exceptions.TooManyRedirects:
#            requests.status_code = "Connection refused"
    else:
        print('Web site does not exist')

with open('Non_Existing_In_Salesforce_Accounts_domains_only_02_7_of_7.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
       demo = str(row)
       demo = demo.strip("[]'")
       demofoo = ("http://" + demo)
       DoesExist(demofoo) 
    csvDataFile.close()

   
#with open('gooddomain.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    print(Fuego)
#    writer.writerows(Fuego)
#    file.close()
