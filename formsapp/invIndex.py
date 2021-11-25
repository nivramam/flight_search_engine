"""
Automatically
generated
by
Colaboratory.

Original
file is located
at
https: // colab.research.google.com / drive / 1
xXcmoQqGqkyZv48wn4VcZvCPK6kbKD2t
"""

import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
# from striprtf.striprtf import rtf_to_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import json

def remove_punctuations(text):
    text=text.lower()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punc:
            text=text.replace(i,"")
    return text

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def union(lst1, lst2):
    return list(set(lst1 + lst2))

def getInvertedIndex():
    documents=[]
    filename = "D:\\Nivedhithaa\\Ninth Semester\\lab\\irrLab\\data\\citiesData\\Agra_wiki.txt";
    infile = open(filename, encoding="utf-8")

    while(True):
        line = infile.readline()
        if not line:
            break
        documents.append(line)

    documents=documents[1:-2]

    for i in range(len(documents)):
        documents[i] = remove_punctuations(documents[i])
        text_tokens = word_tokenize(documents[i])
        documents[i] = [word for word in text_tokens if not word in stopwords.words()]

    print(documents[0])

    total_tokens=[]
    for i in range(len(documents)):
        for j in documents[i]:
            if j not in total_tokens:
                total_tokens.append(j)

    print("The length of terms is",len(total_tokens))
    print("Few among the terms include",end=" ")
    print(*total_tokens[-10:],sep=", ")

    termDict={}
    for i in total_tokens:
        temp=[]
        for j in range(len(documents)):
            if i in documents[j]:
                temp.append(j+1)
        termDict[i]=temp

    printing = dict(list(termDict.items())[0:20])
    inverted_index = json.dumps(printing)
    with open("D:\\Nivedhithaa\\Ninth Semester\\lab\\irrLab\\data\\citiesData\\agra_inv_index.txt", "w") as outfile:
        outfile.write(inverted_index)
    print("The first 10 dictionary terms and their posing lists are")
    for i in printing:
        print(i,":",printing[i],end="\n\n")

    print(f"Query 1: To find the documents which contains fort and tomb")
    print(intersection(printing['fort'], printing['tomb']))
    print(f"Query 1: To find the documents which contains fort or tomb")
    print(union(printing['fort'], printing['tomb']))
getInvertedIndex()