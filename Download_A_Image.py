# go to project settings = > project interpreter => install beautifullscrapper

# using random to generate random name for the image
import random

# importing URLLIB (LIBRARY DOR DOWNLOADING FROM URL) то use the ability to download from url
import urllib.request

# generating method for downloading
def download_image(url):
# generating random name
    name = random.randrange(1,1000)
# concatenating name and extention
    full_Name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_Name)

#calling the method and insert the image Url
download_image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB128Zuo.img")
