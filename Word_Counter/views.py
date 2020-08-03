from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(request):
    return render(request, 'Home.html')

def Count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #Add to dictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'Count.html', {'fulltext':fulltext, 'Count':len(wordlist), 'sortedWords':sortedWords})

def About(request):
    return render(request, 'About.html')
