from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from formsapp import vsm
from formsapp import recommendation
# Create your views here.
text = ''
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
    context = {'data' : str(output)}
    return render(request, "renderOUT.html", context)

def getRecom(request):
    # data = str(request.POST.get('quantity'))
    words = text.split(' ')
    # make ready the query needed for recommendation
    rec_query = helper(words)
    print(rec_query)
    # output = recommendation.recEngine(rec_query['from'], rec_query['to'])
    output = recommendation.recEngine(rec_query['from'], rec_query['to'])
    context = {'data' : str(output)}
    return render(request, "recomm.html", context)
