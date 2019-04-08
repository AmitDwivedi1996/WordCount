from django.http import HttpResponse
from django.shortcuts import render
import operator
def homePage(request):
    return render(request, "BookHome.html")
def count(request):
    data = request.GET["textarea"]
    wordlist = data.split()
    length = len(wordlist)
    datadir = {}
    for word in wordlist:
        if word in datadir:
            datadir[word] += 1 
        else:
            datadir[word] = 1
        sortit = sorted(datadir.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"dataname":data, "fulltext":length, "dict":sortit})

def about(request):
    return render(request, "FAbout.html")