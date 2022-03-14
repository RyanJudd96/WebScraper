import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

URL = "https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E532&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
#browser = webdriver.Chrome()
page = r.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
property_search = soup.find(id="propertySearch")
container = property_search.find(id="propertySearch-results-container")
search_results = container.find(id="l-searchResults")
house_listings = search_results.find_all('div', class_="l-searchResult is-list")

for house_listing in house_listings:
    address_element = house_listing.find('meta', itemprop="streetAddress")
    bed_element = house_listing.find_all('span'[2])
    #bed_element = house_listing.find('span', {"class": "text"})
    #bed_element = house_listing.find('div', class_="property-information")
    #bed_no = bed_element.get_text()
    price_element = house_listing.find("div", class_="propertyCard-priceValue")

    print(address_element['content'])
    print(bed_element)
    print(price_element.text)
    print()