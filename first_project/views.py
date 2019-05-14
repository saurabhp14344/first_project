from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')

def count(request):
    fulltext=request.GET['fulltext']
    counttxt=fulltext.split()
    worddict={}
    for words in counttxt:
        if words in worddict:
            worddict[words] +=1
        else:
            worddict[words]=1
    return render(request,'count.html',{'txt':fulltext ,'countword':len(counttxt), 'worddictionary':worddict})

def aboutus(request):
    return render(request,'aboutus.html')