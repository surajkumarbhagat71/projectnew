from django.shortcuts import render,redirect
from django.views.generic import  View, TemplateView
from .models import *

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re


# Create your views here.

class Home(TemplateView):
    template_name = 'getdata.html'


#--------------------------------------Soluction ---------------------------


# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# listUrls = ["https://www.eventbrite.com/"]
# # browser = webdriver.PhantomJS('/usr/local/bin/phantomjs')
# browser = webdriver.Chrome("./chromedriver")
# urls=[]
#
# for url in listUrls:
#     browser.get(url)
#     soup = BeautifulSoup(browser.page_source,"html.parser")
#     results = soup.findAll('a',{'class':"eds-event-card-content__action-link"})
#     for result in results:
#         link = result["href"]
#         urls.append(link)
#     print(urls)

#-------------------------------------------------------------------


def work(url):
    browser = webdriver.Chrome("./chromedriver")
    urlslist = []
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    results = soup.findAll('a', {'class':"eds-event-card-content__action-link"})
    for result in results:
        link = result["href"]
        urlslist.append(link)

    print(urlslist)
    return urlslist


class GetData(View):
    def post(self,request):
        urls = request.POST.get('url')
        data = work(urls)

        event = EventDetail()

        for x in data:
            res = x
            soup = BeautifulSoup(res,'html.parser')

            span_title = soup.find('h1', {'class': 'listing-hero-title'})
            span_date = soup.find('p', {'class': 'js-date-time-first-line'})
            span_location = soup.find('p', {'class': 'eds-text-weight--heavy'})

            print(span_location)
            print(span_date)
            print(span_title)

            event.url = Url(x)
            event.title = span_title
            event.datetime = span_date
            event.location = span_location
            event.save()

        return render(request,'alllist.html')











