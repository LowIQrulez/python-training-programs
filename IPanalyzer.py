def ipanalyzer ():
    
    #import libraries needed for html scraping
    import requests
    import urllib.request
    from bs4 import BeautifulSoup

    #definition of website from which will data be scraped
    url = "https://www.myip.com/"

    #checking accessability of website, 200 okay, 403 forbidden
    response = requests.get (url)

    #class for library assignment to variable
    soup = BeautifulSoup (response.text,"html.parser")

    #function used from library to find all "span" tags
    soup.findAll ("span")

    #creation of variable from tag containing IP
    iptag = soup.findAll ("span") [0]

    #cration of string containing IP, changing to list divided by signs <,> and then pulling a element containing only ip
    ipstr = str (iptag)
    ipstr = ipstr.split (">") [1]
    ipstr = ipstr.split ("<") [0]

    #the same for country, town and service provider

    countrytag = soup.findAll ("div") [23]

    countrystr = str (countrytag)
    countrystr = countrystr.split (">") [1]
    countrystr = countrystr.split ("<") [0]

    sptag = list (soup.findAll ("div") [17]) [2]

    spstr = sptag.split ("\n") [1]
    spstr = spstr.replace (". ",".")

    print ("IP is: " + ipstr + "\n"
           "Registered in: " + countrystr + "\n"
           "Provided by: " + spstr)
    
ipanalyzer ()