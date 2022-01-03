
#Python code to illustrate parsing of XML files 
# importing the required modules 
import csv 
import requests 
import xml.etree.ElementTree as ET 
  
def loadRSS(): 
  
    # url of rss feed 
    url ='https://www.govevents.com/events.xml'
  
    # creating HTTP response object from given url 
    resp = requests.get(url) 
  
    # saving the xml file 
    with open('eventsmod.xml', 'wb') as f: 
        f.write(resp.content) 
          
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for news items 
    newsitems = [] 
  
    # iterate news items 
    for item in root.findall('./channel/item'): 

        # empty news dictionary 
        news = {} 
  
        # iterate child elements of item 
        for child in item: 
  
                news[child.tag] = child.text.encode('utf8') 
  
        # append news dictionary to news items list 
        newsitems.append(news) 

    # return news items list 
    return newsitems
  
def modifynewsitems(newsitems):
    i = 0
    a = ""
    b = ""
    while i < len(newsitems):
        print(i)
        y = newsitems[i] 
        y.update({'pubDate' : ''})
        a = y["description"]
        a2 = str(a)
        b = y["pubDate"]
        b2 = str(b)
        a2,b2 = a2.split('<br />',1)
        a2 = a2.lstrip('b\'')
        print(a2)
        b2 = b2.rstrip('\'')
        print(b2)
        print(y)
        a3 = {'description' : b2}
        b3 = {'pubDate' : a2}
        newsitems[i].update(a3)
        newsitems[i].update(b3)
        print (y["description"])
        print (y["pubDate"])
        print (y)
        i += 1  
    else:
        print("something broke" + str(i))
    
    return newsitems
  
def savetoCSV(newsitems, filename): 
  
    # specifying the fields for csv file 
    fields = [ 'title', 'link', 'guid', 'description','pubDate'] 
    
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader()
        writer.writerows(newsitems)        

def savetoXML(newsitems, filename):
    # create element tree object 
    tree = ET.parse(filename) 
  
    # get root element 
    root = tree.getroot() 
    i = 0
    for item in root.findall('./channel/item'): 
        for child in item:
            y = newsitems[i]
            for description in item.iter('description'): 
                print(i)
                print(y["description"])
                print(y["pubDate"])
                root.set('description',y["description"])
                print(y["pubDate"])
                pubdate = root.item('eventsmod.xml','pubDate')
                pubdate.text = y["pubDate"]
                root.insert(4,pubdate)
            i += 1
    tree.write(filename)
def main(): 
    # load rss from web to update existing xml file 
    loadRSS() 
  
    # parse xml file 
    newsitems = parseXML('eventsmod.xml') 
    
    modifynewsitems(newsitems) 
  
    # store news items in a csv file 
    savetoCSV(newsitems, 'events.csv') 

    savetoXML(newsitems, 'eventsmod.xml')
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 
