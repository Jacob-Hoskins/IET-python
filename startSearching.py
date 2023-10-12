import json
import os
import requests
from bs4 import BeautifulSoup

items_in_search_list = []
# follow hd with /s/item name to search
home_depot = 'https://homedepot.com/s/{item}?NCNI-5'
# follow l with /search?searchTerm= item name to search
lowes = 'https://www.lowes.com/search?searchTerm={item}'
# 
menards = 'https://www.menards.com/main/search.html?search={item}'
tileShop = 'https://www.tileshop.com/application/floor'

def create_headers():
    response = requests.get(
        url='https://headers.scrapeops.io/v1/browser-headers',
        params={
            'api_key': 'a76a84bb-cba1-45f0-a3f0-a234eb6444e2',
            'num_headers': '2'}
    )
    x = response.json()
    # print(x['result'][1])
    return x['result'][1]

def make_request_menards(itemToSearch):
    print("IN REQUEST")
    final_url = menards.format(item=itemToSearch)
    # response = requests.get('https://www.tileshop.com/application/floor')
    response = requests.get(url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': 'a76a84bb-cba1-45f0-a3f0-a234eb6444e2',
        'url': final_url,
        'render_js': True,
    }, headers=create_headers())
    soup = BeautifulSoup(response.content, 'html5lib')
    # print(soup.prettify(), '\n\n -------- \n\n')
    # print(soup.content, "\n\n---------------------------------------------\n\n")
    # format_menards(soup.find('div', attrs={'class' : 'pricing-info'}))
    # print(soup.find('div', attrs={"id": "searchItems"}), "\n\n -------- \n\n")
    menardsPrice = format_menards(soup.find('div', attrs={"id": "searchItems"}))
    # print(soup.find('div', attrs={"class": "search-item"}))
    # print(menardsMainDiv)
    # print(soup.prettify())
    # print(response.content)
    #response.content
    # print(response.content)
    return menardsPrice



def make_request_lowes(itemToSearch):
    testList = []
    print("IN REQUEST")
    final_url = lowes.format(item=itemToSearch)
    response = requests.get(url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a76a84bb-cba1-45f0-a3f0-a234eb6444e2',
            'url': final_url,
            'render_js': True,
        }, headers=create_headers())
    soup = BeautifulSoup(response.content, 'html5lib')
    # print(soup.find('div', attrs={'data-selector': 'splp-prd-act-$'}))
    # test = soup.find('div', attrs={'class': 'prdt-actl-pr'})
    test = soup.find('div', attrs={'class': 'tile_group'})
    contentSection= soup.find('section', attrs={'id': 'listItems'})
    # print(contentSection.find('div', attrs={'data-selector': 'splp-prd-act-$'}))
    for x in contentSection:
        testList.append(x)

    print(test)

    # for x in test:
    #     print(x)

def format_lowes(priceDiv):
    pass

def format_menards(priceDiv):
    # print(priceDiv, '\n\n-----\n\n')
    listOfResultItems = []
    firstItemPrice = []

    if(priceDiv != None):
        # print(priceDiv, '\n\n ----- \n\n', list(priceDiv))
        new_type = str(priceDiv)
        new_list = new_type.split("</")
        for x in new_list:
            if('heading' in x):
                menardsItemName = x.split('>')[-1]
                listOfResultItems.append(menardsItemName)
            if('pricing-info' in x):
                menardsItemPrice = x.split('\n')[-2]
                final_price_form = menardsItemPrice.split(' ')[-1]
                listOfResultItems.append(final_price_form)

        firstItemPrice.append({'itemName': listOfResultItems[0], 'itemPrice': listOfResultItems[1]})
        # print(listOfResultItems[0], listOfResultItems[1])
        return firstItemPrice[0]
        # return listOfResultItems

    elif(priceDiv == None):
        #TODO: in future a dictionary will be passed along the funcs and will have the item being searched that should be used
        # here and to restart the search process
        print("NoneType Error, couldnt properly receieve response")


def search_home_depot(itemToSearch):
    print("IN REQUEST")
    final_url = home_depot.format(item=itemToSearch)
    response = requests.get(url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a76a84bb-cba1-45f0-a3f0-a234eb6444e2',
            'url': final_url,
            'render_js': True,
        }, headers=create_headers())
    soup = BeautifulSoup(response.content, 'html5lib')
    soupContent = soup.find('section', attrs={'id': 'browse-search-pods-1'})
    # print(soupContent)
    for x in soupContent:
        unformattedNames = x.find('div', attrs={'data-component': 'ProductHeader'})
        print(unformattedNames)
        #Below gets prices
        unformattedPrices = x.find('div', attrs={'class': 'price'})
        test = str(unformattedPrices)
        testToList = test.split("</")
        firstNumber = testToList[1].split(">")
        secondNumber = testToList[3].split(">")
        shownPrice = firstNumber[-1], '.', secondNumber[-1]

def search_for_items_starting_point(doc_info):
    for x in doc_info["itemList"]:
        items_in_search_list.append(x["itemName"])

    return items_in_search_list

# make_request_menards("hardwood%20flooring")
# make_request_lowes("hardwood%20flooring")
# create_headers()
search_home_depot("dark%20oak%20hardwood%20flooring")
