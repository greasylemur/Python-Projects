#!/usr/bin/python
print "Content-type: text/html\n\n";

import cgi; 
import time;
import webbrowser;
import cgitb;
cgitb.enable();

##Just A Few Variables
auction1 = 0
auction2 = 0
auction3 = 0
auction4 = 0
auction5 = 0
auction6 = 0

form = cgi.FieldStorage();
PARMS = form["searcher"].value;
if "Auction1" in form:
 auction1 = form["Auction1"].value;
if "Auction2" in form:
 auction2 = form["Auction2"].value;
if "Auction3" in form:
 auction3 = form["Auction3"].value;
if "Auction4" in form:
 auction4 = form["Auction4"].value;
if "Auction5" in form:
 auction5 = form["Auction5"].value;
if "Auction6" in form:
 auction6 = form["Auction6"].value;

SPARMS = PARMS.replace(" ","%20");
PARMSPLUS = PARMS.replace(" ","+");
tplus = str(time.strftime("%X.000"));
tplus = tplus.replace(":", "%3A");
YMD = str(time.strftime("%Y-%m-%d"));
d = str(time.strftime("%d"));
m = str(time.strftime("%m"));
y = str(time.strftime("%Y"));
Livedate = YMD+"T"+tplus;
EDate = d+"%2f"+m+"%2f"+y;
SDate = d+"%2f"+m+"%2f2013";

invaluable = "http://www.invaluable.com/catalog/searchLots.cfm?scp=p&catalogRef=&shw=50&ord=0&img=0&olF=1&houseRef=&houseLetter=A&artistRef=&areaID=&countryID=&regionID=&stateID=&fdt=0&tdt=0&fr=0&to=0&wa="+SPARMS+"&wp=&wo=&nw=&upcoming=0&rp=&hi=1&rem=FALSE&cs=0&ns=0&isSC=0&row=1";
southbys = "http://www.sothebys.com/en/search.html?keywords="+SPARMS+"&ex_currency=USD&startDate="+SDate+"&endDate="+EDate+"&ex_soldPR=soldPR#keywords="+PARMS;
gemrockauctionslive = "http://www.gemrockauctions.com/search?keywords="+PARMSPLUS+"&start_bid_min=&start_bid_max=&closed=1&length_min=&length_max=&width_min=&width_max=&depth_min=&depth_max=&weight_min=&weight_max=&order=new&view=";
addall_kword = "http://used.addall.com/SuperRare/submitRare.cgi?author=&title=&keyword="+PARMSPLUS+"&isbn=&order=PRICE&ordering=ASC&binding=Any+Binding&min=&max=&exclude=&match=Y&dispCurr=USD&timeout=20&store=ABAA&store=Alibris&store=Abebooks&store=AbebooksAU&store=AbebooksDE&store=AbebooksFR&store=AbebooksUK&store=Amazon&store=AmazonCA&store=AmazonUK&store=AmazonDE&store=AmazonFR&store=Antiqbook&store=Biblio&store=BiblioUK&store=Bibliophile&store=Bibliopoly&store=Booksandcollectibles&store=ILAB&store=Half&store=LivreRareBook&store=Powells&store=Wbm&store=ZVAB";
liveauctioneers = "http://www.liveauctioneers.com/search?q="+SPARMS+"&by_date="+Livedate+"Z&sort=relevance&dtype=gallery&hasimage=true&type=complete&rows=120";
auctionzip = "http://www.auctionzip.com/cgi-bin/auctionsearch.cgi?month=&year=&newsearch=1&txtSearchRadius=30&txtSearchZip=22046&txtSearchKeywords="+PARMSPLUS+"&idxSearchCategory=0";

##Just Making Some Html and Java
print "<html><head> <script> function myFunction() {";
if auction1 == "on":
 print "window.open('"+liveauctioneers+"');";
if auction2 == "on":
 print "window.open('"+invaluable+"');";
if auction3 == "on":
 print "window.open('"+southbys+"');";
if auction4 == "on":
 print "window.open('"+auctionzip+"');";
if auction5 == "on":
 print "window.open('"+gemrockauctionslive+"');";
if auction6 == "on":
 print "window.open('"+addall_kword+"');";
print "} </script>";
print "<title>Search Python</title>";
print "</head><body onload='myFunction()'>";
print "<p>Test page using Python</p>";

print form;
print auction1;
print auction2;
print auction3;
print auction4;
print auction5;
print auction6;

print "liveauctioneers URL: "+liveauctioneers+"</br>";
print "invaluable URL: "+invaluable+"</br>";
print "Southbys URL: "+southbys+"</br>";
print "GemRock Auctions URL: "+gemrockauctionslive+"</br>";
print "add all URL: "+addall_kword+"</br>";
print "auction zip URL: "+auctionzip+"</br>";

print "tplus Value: "+tplus+"</br>";
print "YMD Value: "+YMD+"</br>";
print "PARMS Value: "+PARMS+"</br>";
print "SPARMS Value: "+SPARMS+"</br>";
print "PARMSPLUS Value: "+PARMSPLUS+"</br>";
print "d Value: "+d+"</br>";
print "m Value: "+m+"</br>";
print "y Value: "+y+"</br>";
print "Livedate Value: "+Livedate+"</br>";
print "EDate Value: "+EDate+"</br>";
print "SDate Value: "+SDate+"</br>";
print "<p>done</p>";
print "</body></html>";