from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from formsapp import vsm
from formsapp import recommendation
from formsapp import weatherRecommendation
from formsapp import clustering
import json
import csv
import pandas as pd
# Create your views here.
text = ''
citySimilars= []
def index(request):
    return render(request, "index.html")

def helper(a):
    rec_query = {'from' : '', 'to' : ''}
    for i in range(len(a)):
        if(a[i]=="to"):
            rec_query['from'] = a[i-1]
            rec_query['to'] = a[i+1]
    return rec_query

def saveCriteria(request):
    context = {}
    data = str(request.POST.get('quantity'))
    print(data)
    global text
    text = data
    output = vsm.handleQuery(data)
    indexDocs = vsm.getDocsGivenIndices(output.tolist())
    print(indexDocs)

    context = {'data' : str(output), 'docsRelevance' : indexDocs}
    return render(request, "renderOUT.html", context)

def getRecom(request):
    # data = str(request.POST.get('quantity'))
    words = text.split(' ')
    # make ready the query needed for recommendation
    rec_query = helper(words)
    print(rec_query)
    # output = recommendation.recEngine(rec_query['from'], rec_query['to'])
    output = recommendation.recEngine(rec_query['from'], rec_query['to'])
    output = output.strip('][').split(', ')
    # cityRecommendation must contain the recommendation of cities
    weather_OUTPUT = weatherRecommendation.getWeather(rec_query['to'])
    context = {'cityFrom': rec_query['from'], 'cityTo': rec_query['to'], 'data' : output, 'weatherRecom' : weather_OUTPUT}
    return render(request, "recomm.html",context)

def clusterBasedOnAQI(request):
    citiesList = []
    with open("D:\\Nivedhithaa\\Ninth Semester\\lab\\irrLab\data\\top_tourists.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            citiesList.append(row[0])
    df = pd.read_excel('D:\\Nivedhithaa\\Ninth Semester\\lab\\irrLab\\irPackage\\formsproject\\AQI_Bulletin_20211124_converted_by_abcdpdf.xlsx',engine='openpyxl')
    # print(df.head())
    df.drop(['Prominent Pollutant', 'Based on Number of Monitoring Stations'], 1, inplace=True)
    for k in list(df):
        df[k] = pd.to_numeric(df[k], errors='ignore')
    df.fillna(0, inplace=True)
    df = clustering.handle_cat_data(df)
    sorted_df = df.sort_values(by='Air Quality')
    print(sorted_df.head(20))
    context = {'output': sorted_df.head() }
    return render(request, "clus.html", context)