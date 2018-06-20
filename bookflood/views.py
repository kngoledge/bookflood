from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView
from bookflood.models import UserProfile, Book

class BookView(View): 
    model=Book

class BookCreate(BookView, CreateView): 
    fields=['title', 'author', 'isbn', 'genre', 'language']

class BookList(BookView, ListView): 
    template_name='book.html'

class PeopleList(ListView): 
    model=UserProfile
    template_name='home.html'

class BookDetail(BookView, DetailView): 
    pass
    model=Book
    

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

