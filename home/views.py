from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import time
import urllib3

from . scripts import forms

urllib3.disable_warnings()

# defined location
def get_coordinates(address):
    api_key = "AIzaSyBnJ1liZBeenmphZS-bX3P__P3yp-IhTms"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
#     time.sleep(2)
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        return {'latitude' : latitude, 'longitude' : longitude}

def get_restaurant_data(data):
  api_key = "AIzaSyBivWB-SLk-tGj7OnTy433-delKZH0mv00"
#   api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%d&type=restaurant&key=%s"%(str(data['longitude']),str(data['longitude']),data['range'],api_key)
  api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=18.5158057,73.9271644&radius=2000&type=restaurant&key=AIzaSyBivWB-SLk-tGj7OnTy433-delKZH0mv00 "
  api_response = requests.get(api_url)
#   time.sleep(2)
  api_response_dict = api_response.json()
  return api_response_dict['results']

# Create your views here.
def home(request):
  return render(request, 'home/home.html' ,{})

# Calling location
def locate(request):
  address = "Magarpatta, Pune"
  coordinates = get_coordinates(address)
  data = {
    'latitude' : coordinates['latitude'],
    'longitude' : coordinates['longitude'],
    'range' : 2000
  }
  results = get_restaurant_data(data)
  print 'Length ',len(results)
  return render(request, 'home/locate.html' ,{'results':results})

def book_food(request):
  return render(request, 'home/book.html', {})

def book(request):
  api_url = "https://2factor.in/API/V1/f6e7ea01-4488-11e8-a895-0200cd936042/SMS/7503240994/AUTOGEN"
  api_response = requests.get(api_url)
  api_response_dict = api_response.json()
  return render(request, 'home/generated_otp.html', {'results':api_response_dict})

def success(request):
  if request.method == 'POST':
    form = forms.NameForm(request.POST)
  api_url = "https://2factor.in/API/R1/?module=TRANS_SMS&apikey=f6e7ea01-4488-11e8-a895-0200cd936042&to=7503240994&from=Hotels&templatename=Hotel&var1=Mohit&var2=121212"
  api_response = requests.get(api_url)
  api_response_dict = api_response.json()
  return HttpResponseRedirect(request, 'home/success.html', {'form':form})
  #return render(request, 'home/success.html',{'name' : 'Mohit'})