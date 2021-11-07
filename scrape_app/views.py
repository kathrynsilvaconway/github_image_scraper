from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as bs

def index(request):
    return render(request, 'index.html')

def find_pic(request):
    user = request.POST['user']
    link = f"https://github.com/{user}/"
    request.session['link'] = link
    print(request.session['link'])
    return redirect('/display_pic')

def display_pic(request):
    link = request.session['link']
    get_it = requests.get(link)
    pick_it = bs(get_it.content, 'html.parser')
    image = pick_it.select('img.avatar.avatar-user')[0]['src']
    context = {
        'image': image
    }
    return render(request, 'display_pic.html', context)
# Create your views her
