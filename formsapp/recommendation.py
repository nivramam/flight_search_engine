import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import csv
# from io import StringIO

def remove_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    for data in soup(['span']):
        # Remove tags
        data.decompose()
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

def recEngine(fromCity, toCity):
    base_url='https://www.goibibo.com/flights/'
    base_url = base_url + "/{}-to-{}-flights/"
    url = base_url.format(fromCity, toCity)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # soup.find('div', {'class':'footer-wrapper_links'}).find_all('a')
    recommendations = []
    # if(soup.find('div', {'class': 'common-stylesstyles__CommonDetails-sc-uferee-1 list-for-linksstyles__Details-sc-18mazeo-0 jVkNuU IEHrn'}) == 'NoneType')
    #     flag =
    for i in soup.find('div', {'class': 'common-stylesstyles__CommonDetails-sc-uferee-1 list-for-linksstyles__Details-sc-18mazeo-0 jVkNuU IEHrn'}):
        # print(i)
        recommendations.append(i)
    # print(link)
    recommendations = remove_tags(str(recommendations))
    return recommendations

# print(recEngine("bangalore", "coimbatore"))
# print(type(recEngine("bangalore", "coimbatore"))