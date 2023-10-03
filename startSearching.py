import os
import requests
import bs4

items_in_search_list = []
home_depot = 'https://homedepot.com'
lowes = 'https://www.lowes.com'
# 
menards = 'https://www.menards.com/search.html?search={item}'
tileShop = 'https://www.tileshop.com/application/floor'

# URL of site to search goes into the params section
# TODO: create new headers everytime a search is made to help scrapper reliablity
def make_request(itemToSearch):
    print("IN REQUEST")
    print(menards.format(item=itemToSearch[0]))
    # response = requests.get('https://www.tileshop.com/application/floor')
    # response = requests.get(url='https://proxy.scrapeops.io/v1/',
    # params={
    #     'api_key': '02192b24-dbdb-456f-95c3-46dcfffdeb40',
    #     'url': menards,
    # },)
    # print(response.content)

def search_lowes():
    pass

def search_menards():
    pass

def search_home_depot():
    pass

def search_for_items_starting_point(doc_info):
    for x in doc_info["itemList"]:
        items_in_search_list.append(x["itemName"])

    return items_in_search_list

