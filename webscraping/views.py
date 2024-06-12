from django.http import JsonResponse
import requests
from django.shortcuts import render
from datetime import datetime, timezone
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import datetime
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from .weatherutils import *
from .doubtresolve import *
from .movieorhero import *
from .pricecomparator import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('id_username')  # Get username from POST data
        password = request.POST.get('id_password')  # Get password from POST data
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index2')
        else:
            # Handle invalid credentials
            return JsonResponse({'success': False, 'error': 'Invalid username or password'}, status=400)
    else:
        # Handle GET request (if needed)
        pass





def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            UserProfile.objects.create(user=user)
            return redirect('/index/')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'weather/index.html', {'form': form})

import requests
from bs4 import BeautifulSoup


def home(request):
    
    if request.user:
        return render(request, 'weather/index5.html')
    else :
        return render(request,'weather/index.html')

def index2(request):
    if request.user.is_authenticated:
        return render(request, 'weather/index2.html')
    else :
        return render(request,'weather/index.html')
def index7(request):
    if request.user.is_authenticated:
        print(request.user)
        return render(request, 'weather/index7.html')
    else :
        return render(request,'weather/index.html')

def index8(request):
    if request.user.is_authenticated:
        print(request.user)
        return render(request, 'weather/index8.html')
    else :
        return render(request,'weather/index.html')
def index10(request):
    if request.user.is_authenticated:
        print(request.user)
        return render(request, 'weather/index10.html')
    else :
        return render(request,'weather/index.html')
def index5(request):
    if request.user.is_authenticated:
        return render(request, 'weather/index5.html')
    else :
        return render(request,'weather/index.html')

def index4(request):
    if request.user.is_authenticated:
        return render(request, 'weather/index4.html')
    else :
        return render(request,'weather/index.html')

def index3(request):
    if request.user.is_authenticated:
        return render(request, 'weather/index3.html')
    else :
       return render(request,'weather/index.html')

def index6(request):
    if request.user.is_authenticated:
        print("hi")
        return render(request, 'weather/index6.html')
    else :
        return render(request,'weather/index.html')
        

def index9(request):
    if request.user.is_authenticated:
        return render(request, 'weather/index9.html')
    else :

        return render(request,'weather/index.html')

def index(request):
    return render(request, 'weather/index.html')

@login_required
def weather(request, city_name):
    location = city_name
    if location:
        todaytemp,weather_data = get_weather_info(location,request.user)

        if weather_data:
            print(weather_data)
            return JsonResponse({'weather_data': weather_data,'today_temp':todaytemp})
        else:
            error_message = 'Error fetching weather data. Please try again.'
            return JsonResponse({'error_message': error_message})
    else:
        return JsonResponse({'error_message': 'Please enter a city name.'})


@login_required
def doubt(request,doubt):
    if doubt :
        answers=doubtscrape(doubt,request.user)
        if answers:
            print(answers)
            return JsonResponse({'answers':answers})
        else :
            error_message = 'error fetching data'
            return JsonResponse({'error_message':error_message})
    else :
        return JsonResponse({'error_message': 'Please enter a doubt'})
    
@login_required
def movien(request,searchTerm):
    if searchTerm :
        answers=get_movie_info(searchTerm,request.user)
        if answers:
            print(answers)
            return JsonResponse({'answers':answers})
        else :
            error_message = 'error fetching data'
            return JsonResponse({'error_message':error_message})
    else :
        return JsonResponse({'error_message': 'Please enter a movie name '})
    
@login_required
def actorn(request,searchTerm):
    if searchTerm :
        answers=get_actor_filmography(searchTerm)
        if answers:
            print(answers)
            return JsonResponse({'answers':answers})
        else :
            error_message = 'error fetching data'
            return JsonResponse({'error_message':error_message})
    else :
        return JsonResponse({'error_message': 'Please enter a movie name '})
    
@login_required
def doubtn(request,searchTerm):
    if searchTerm :
        answers=doubtscrape(searchTerm,request.user)
        if answers:
            print(answers)
            return JsonResponse({'answers':answers})
        else :
            error_message = 'error fetching data'
            return JsonResponse({'error_message':error_message})
    else :
        return JsonResponse({'error_message': 'Please enter a movie name '})

@login_required
def pricen(request,searchTerm):
    if searchTerm :
        answers=price_comparator(searchTerm,request.user)
        if answers:
            print(answers)
            return JsonResponse({'answers':answers})
        else :
            error_message = 'error fetching data'
            return JsonResponse({'error_message':error_message})
    else :
        return JsonResponse({'error_message': 'Please enter a movie name '})
    

from django.shortcuts import render

def price_comparator_history(request):
    history_entries = pricecomparator.objects.filter(user_id=request.user)

    history_data = [{'productname': entry.productname, 'price': entry.price, 'productlink': entry.productlink} for entry in history_entries]

    return JsonResponse(history_data, safe=False)


@login_required
def doubt_resolve_history(request):
    current_user = request.user
    doubts = doubtResolve.objects.filter(user_id=current_user)
    doubts_data = []

    for doubt in doubts:
        doubt_data = {
            'doubt': doubt.doubt,
            'answers': [
                {'url': doubt.url1, 'answer': doubt.answer1},
                {'url': doubt.url2, 'answer': doubt.answer2},
                {'url': doubt.url3, 'answer': doubt.answer3}
            ]
        }
        doubts_data.append(doubt_data)

    return JsonResponse(doubts_data, safe=False)


def movie_history(request):
    movies = movie.objects.filter(user_id=request.user)
    movie_data = [{'title': movie.title, 'rating': movie.rating, 'summary': movie.summary} for movie in movies]
    return JsonResponse(movie_data, safe=False)

from django.http import JsonResponse
from .models import Weather

def weather_search_history(request):
    # Retrieve weather search history
    history_entries = Weather.objects.all()

    # Convert queryset to a list of dictionaries
    history_data = []
    for entry in history_entries:
        data_entry = {
            'Location': entry.location,
            'Date 1': entry.date1,
             "temp 1":entry.temp1,
            'Date 2': entry.date2,
            'High Temp 2': entry.hightemp2,
            'Low Temp 2': entry.lowtemp2,
            'Date 3': entry.date3,
            'High Temp 3': entry.hightemp3,
            'Low Temp 3': entry.lowtemp3,
            'Date 4': entry.date4,
            'High Temp 4': entry.hightemp4,
            'Low Temp 4': entry.lowtemp4,
            'Date 5': entry.date5,
            'High Temp 5': entry.hightemp5,
            'Low Temp 5': entry.lowtemp5,
            'Date 6': entry.date6,
            'High Temp 6': entry.hightemp6,
            'Low Temp 6': entry.lowtemp6,
            'Date 7': entry.date7,
            'High Temp 7': entry.hightemp7,
            'Low Temp 7': entry.lowtemp7,
            'Date 8': entry.date8,
            'High Temp 8': entry.hightemp8,
            'Low Temp 8': entry.lowtemp8,
            'Date 9': entry.date9,
            'High Temp 9': entry.hightemp9,
            'Low Temp 9': entry.lowtemp9,
            'Date 10': entry.date10,
            'High Temp 10': entry.hightemp10,
            'Low Temp 10': entry.lowtemp10,
        }
        history_data.append(data_entry)

    return JsonResponse(history_data, safe=False)

from django.contrib.auth import logout
from django.http import JsonResponse

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
