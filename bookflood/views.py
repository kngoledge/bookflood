from django.shortcuts import render
from bookflood.models import UserProfile, Book

def home(request):
   user_profiles = UserProfile.objects.all()
   data = { 'people': user_profiles
           }
   return render(request, 'home.html', data)

def view_person(request): 
    person = UserProfile.objects.get(id=1)
    data = {'person' : person} 
    return render(request, 'person.html', data)

def view_book(request): 
    books = Book.objects.all()
    data = {'books': books} 
    return render(request, 'book.html', data) 
