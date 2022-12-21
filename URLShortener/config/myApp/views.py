from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
import clipboard


def hash(url):
    p = 97
    m = 10**9 + 9
    res = 0
    pow_p = 1
    for i in url:
        res = (res + (ord(i) + 1) * pow_p) % m
        pow_p = (p*pow_p)%m
    return res

def shortener(url):
    urlValue = hash(url)
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""
    while(urlValue > 0):
        shortURL += map[urlValue%62]
        urlValue //= 62
    return shortURL

def display(request):
    if request.POST.get("copyBtn"):
        fetchResult = request.POST['shortURL']
        clipboard.copy(str(fetchResult))
    return render(request, 'myApp/index.html')

def urlResult(request):
    urlConvert = True
    originURL = request.POST['originURL']
    outputOfQuery = []
    if not originURL.startswith('http'):
        outputOfQuery.append({'shortURL': "실패"})
        return render(request, 'myApp/urlResult.html', {"urlConvert": urlConvert, "output": outputOfQuery})
    shortURL = "http://127.0.0.1:8000/" + shortener(originURL)
    try:
        with connection.cursor() as cursor:
            sqlQuery = "insert into url (originHash, originURL, shortURL) values " \
            "('" + str(hash(originURL)) + "', '" + originURL + "', '" + shortURL + "');"
            cursor.execute(sqlQuery)
            connection.commit()
            connection.close()
            outputOfQuery.append({'shortURL': shortURL})
        return render(request, 'myApp/urlResult.html', {"urlConvert": urlConvert, "output": outputOfQuery})

    except:
        with connection.cursor() as cursor:
            sqlQuery = "select shortURL from url where originURL = '" + originURL + "';"
            cursor.execute(sqlQuery)
            fetchResult = cursor.fetchall()
            connection.commit()
            connection.close()
            for temp in fetchResult:
                eachRow = {'shortURL': temp[0]}
                outputOfQuery.append(eachRow)
        return render(request, 'myApp/urlResult.html', {"urlConvert": urlConvert, "output": outputOfQuery})


def origin(request, shortURL):
    outputOfQuery = []
    try:
        with connection.cursor() as cursor:
            sqlQuery = "select originURL from url where shortURL = 'http://127.0.0.1:8000/" + shortURL + "';"
            cursor.execute(sqlQuery)
            fetchResult = cursor.fetchall()
            connection.commit()
            connection.close()
            for temp in fetchResult:
                eachRow = {'shortURL': temp[0]}
                outputOfQuery.append(eachRow)
        return redirect(fetchResult[0][0])
    except:
        return render(request, 'myApp/index.html')

